from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()






class Student(db.Model):
    id = db.column(db.Integer, primary_key = True)
    name = db.column(db.string(60), unique = True, nullable = False)
    email = db.column(db.string(120), unique=True, nullable=False)
    course = db.relationship('Course', secondary='student_course')
    grade = db.relationship('Grade', backref='student_grade', lazy=True)
    def __repr__(self):
        return f"<{self.name}%>"

class Course(db.Model):
    id = db.column(db.Integer, primary_key = True)
    name = db.column(db.string(60), unique = True, nullable = False)
    teacher = db.column(db.string(60), unique = True, nullable = False)
    enrolled_students = db.relationship('User', secondary='students')
    def __repr__(self):
        return f"<{self.name}%>"

class User(db.model):
    id = id = db.column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    courses = db.relationship('Course', secondary='students')
    user_type = db.Column(db.String(20))

    def __repr__(self):
        return f"<{self.name}%>"

class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer(), db.ForeignKey('courses.id'), nullable=False)
    percent_grade = db.Column(db.Float(), nullable=False)
    letter_grade = db.Column(db.String(5), nullable=True)

    def __repr__(self):
        return f"<{self.percent_grade}%>"


