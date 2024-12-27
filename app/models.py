# from .extensions import db

# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(50), unique=True)

#     students = db.relationship("Student", back_populates="course")




# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True)

#     course_id = db.Column(db.ForeignKey("course.id"))

#     course = db.relationship("Course", back_populates="students")




from .extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # Relationship to Student
    students = db.relationship("Student", back_populates="course", cascade="all, delete-orphan")


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # ForeignKey to Course
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    # Relationship to Course
    course = db.relationship("Course", back_populates="students")
