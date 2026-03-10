import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import pandas as pd
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sd-presensi-secret-key-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sd_attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(20), nullable=False)
    academic_year = db.Column(db.String(20), nullable=False)
    students = db.relationship('Student', backref='current_class', lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nisn = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    attendances = db.relationship('Attendance', backref='student', lazy=True)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow().date)
    status = db.Column(db.String(1), nullable=False) # H, S, I, A
    time_in = db.Column(db.Time, default=lambda: datetime.now().time())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Username atau password salah', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    classes = Class.query.all()
    total_students = Student.query.count()
    today = datetime.utcnow().date()
    
    # Counts for each status
    count_h = Attendance.query.filter_by(date=today, status='H').count()
    count_s = Attendance.query.filter_by(date=today, status='S').count()
    count_i = Attendance.query.filter_by(date=today, status='I').count()
    count_a = Attendance.query.filter_by(date=today, status='A').count()
    
    today_attendance = Attendance.query.filter_by(date=today).count()
    # Tambahkan daftar siswa dengan status hari ini
    students = Student.query.all()
    attendance_today = {a.student_id: a.status for a in Attendance.query.filter_by(date=today).all()}
    
    return render_template('dashboard.html', 
                           classes=classes, 
                           total_students=total_students, 
                           today_attendance=today_attendance,
                           count_h=count_h,
                           count_s=count_s,
                           count_i=count_i,
                           count_a=count_a,
                           students=students,
                           attendance_today=attendance_today)

@app.route('/add_class', methods=['POST'])
@login_required
def add_class():
    class_name = request.form.get('class_name')
    academic_year = request.form.get('academic_year')
    
    if class_name and academic_year:
        new_class = Class(class_name=class_name, academic_year=academic_year)
        db.session.add(new_class)
        db.session.commit()
        flash(f'Kelas {class_name} berhasil ditambahkan!', 'success')
    else:
        flash('Data tidak lengkap', 'danger')
        
    return redirect(url_for('students_list'))

@app.route('/add_student', methods=['POST'])
@login_required
def add_student():
    nisn = request.form.get('nisn')
    full_name = request.form.get('full_name')
    gender = request.form.get('gender')
    class_id = request.form.get('class_id')
    
    if nisn and full_name and gender and class_id:
        existing = Student.query.filter_by(nisn=nisn).first()
        if existing:
            flash(f'Error: NISN {nisn} sudah terdaftar!', 'danger')
        else:
            new_student = Student(nisn=nisn, full_name=full_name, gender=gender, class_id=class_id)
            db.session.add(new_student)
            db.session.commit()
            flash(f'Siswa {full_name} berhasil ditambahkan!', 'success')
    else:
        flash('Data siswa tidak lengkap', 'danger')
        
    return redirect(url_for('students_list'))

@app.route('/class/<int:class_id>')
@login_required
def view_class(class_id):
    target_class = Class.query.get_or_404(class_id)
    students = Student.query.filter_by(class_id=class_id).all()
    
    # Get date from query string or default to today
    date_str = request.args.get('date')
    if date_str:
        try:
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            target_date = datetime.utcnow().date()
    else:
        target_date = datetime.utcnow().date()
        
    attendance_data = {a.student_id: a.status for a in Attendance.query.filter_by(date=target_date).all()}
    return render_template('class_detail.html', 
                           target_class=target_class, 
                           students=students, 
                           attendance_data=attendance_data,
                           selected_date=target_date.strftime('%Y-%m-%d'))

@app.route('/submit_attendance', methods=['POST'])
@login_required
def submit_attendance():
    class_id = request.form.get('class_id')
    date_str = request.form.get('attendance_date')
    
    if date_str:
        target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    else:
        target_date = datetime.utcnow().date()
    
    # Simple implementation: update or insert
    students = Student.query.filter_by(class_id=class_id).all()
    for student in students:
        status = request.form.get(f'status_{student.id}')
        if status:
            existing = Attendance.query.filter_by(student_id=student.id, date=target_date).first()
            if existing:
                existing.status = status
            else:
                new_att = Attendance(student_id=student.id, date=target_date, status=status)
                db.session.add(new_att)
    
    db.session.commit()
    flash('Absensi berhasil disimpan!', 'success')
    return redirect(url_for('view_class', class_id=class_id, date=target_date.strftime('%Y-%m-%d')))

@app.route('/students')
@login_required
def students_list():
    classes = Class.query.all()
    all_students = Student.query.all()
    return render_template('students.html', classes=classes, students=all_students)

@app.route('/classes')
@login_required
def classes_list():
    classes = Class.query.all()
    return render_template('classes.html', classes=classes)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/export_excel/<int:class_id>')
@login_required
def export_excel(class_id):
    target_class = Class.query.get_or_404(class_id)
    students = Student.query.filter_by(class_id=class_id).all()
    
    data = []
    for s in students:
        attendances = Attendance.query.filter_by(student_id=s.id).order_by(Attendance.date.desc()).all()
        for att in attendances:
            data.append({
                'Tanggal': att.date,
                'NISN': s.nisn,
                'Nama': s.full_name,
                'L/P': s.gender,
                'Status': att.status,
                'Waktu Input': att.time_in
            })
    
    if not data:
        flash('Belum ada data absensi untuk diekspor.', 'warning')
        return redirect(url_for('view_class', class_id=class_id))
        
    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Absensi')
    
    output.seek(0)
    filename = f"Absensi_{target_class.class_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.xlsx"
    
    return send_file(output, as_attachment=True, download_name=filename, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# Init DB with dummy data
def init_db():
    with app.app_context():
        db.create_all()
        # Create default user if not exists
        if not User.query.filter_by(username='guru').first():
            hashed_pw = bcrypt.generate_password_hash('guru123').decode('utf-8')
            guru = User(username='guru', password=hashed_pw, full_name='Guru MI Aska')
            db.session.add(guru)
            db.session.commit()
            
        # Create dummy class and students only if Class table is empty
        if not Class.query.first():
            cls1 = Class(class_name='Kelas 1-A', academic_year='2023/2024')
            db.session.add(cls1)
            db.session.commit()
            
            # Check if students exist to avoid UNIQUE constraint error
            if not Student.query.filter_by(nisn='12345').first():
                s1 = Student(nisn='12345', full_name='Budi Santoso', gender='L', class_id=cls1.id)
                db.session.add(s1)
            if not Student.query.filter_by(nisn='12346').first():
                s2 = Student(nisn='12346', full_name='Siti Aminah', gender='P', class_id=cls1.id)
                db.session.add(s2)
            if not Student.query.filter_by(nisn='12347').first():
                s3 = Student(nisn='12347', full_name='Agus Setiawan', gender='L', class_id=cls1.id)
                db.session.add(s3)
            db.session.commit()

@app.route('/test')
def test_route():
    return "<h1>Server is Working!</h1>"

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
