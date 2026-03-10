from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum('admin', 'guru', name='user_roles'), default='guru')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with Class (One Teacher can be a Class Teacher)
    managed_classes = db.relationship('Class', backref='teacher', lazy=True)

class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(20), nullable=False)
    academic_year = db.Column(db.String(20), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # Relationship with Students
    students = db.relationship('Student', backref='current_class', lazy=True)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    nisn = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum('L', 'P', name='student_gender'), nullable=False)
    parent_contact = db.Column(db.String(20))
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    
    # Relationship with Attendance
    attendances = db.relationship('Attendance', backref='student', lazy=True)

class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow().date(), nullable=False)
    status = db.Column(db.Enum('H', 'S', 'I', 'A', name='attendance_status'), nullable=False)
    time_in = db.Column(db.Time, default=datetime.now().time())
    notes = db.Column(db.Text)
    attachment = db.Column(db.String(255))
