from app import db
from app.models import Student, Course

def add_data():
    # Create a new course
    new_course = Course(name="Mathematics")
    db.session.add(new_course)
    db.session.commit()

    # Create a new student
    new_student = Student(name="John Doe", course_id=new_course.id)
    db.session.add(new_student)
    db.session.commit()

if __name__ == "__main__":
    add_data()