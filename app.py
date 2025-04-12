from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Course, Faculty, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Helper route to create tables (run once)
@app.route('/create-tables')
def create_tables():
    db.create_all()
    return "Tables created"

# ------------------------- COURSE ROUTES ------------------------- #
@app.route('/add-course', methods=['POST'])
def add_course():
    data = request.get_json()
    new_course = Course(**data)
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"message": "Course added", "course": new_course.to_dict()}), 201

@app.route('/update-course', methods=['PUT'])
def update_course():
    data = request.get_json()
    course = Course.query.get(data.get('code'))
    if not course:
        return jsonify({"message": "Course not found"}), 404
    course.name = data['name']
    course.dept = data['dept']
    course.credits = data['credits']
    db.session.commit()
    return jsonify({"message": "Course updated", "course": course.to_dict()})

@app.route('/delete-course', methods=['DELETE'])
def delete_course():
    code = request.get_json().get('code')
    course = Course.query.get(code)
    if not course:
        return jsonify({"message": "Course not found"}), 404
    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course deleted"})

# ------------------------- FACULTY ROUTES ------------------------- #
@app.route('/add-faculty', methods=['POST'])
def add_faculty():
    data = request.get_json()
    new_faculty = Faculty(**data)
    db.session.add(new_faculty)
    db.session.commit()
    return jsonify({"message": "Faculty added", "faculty": new_faculty.to_dict()}), 201

@app.route('/update-faculty', methods=['PUT'])
def update_faculty():
    data = request.get_json()
    faculty = Faculty.query.get(data.get('id'))
    if not faculty:
        return jsonify({"message": "Faculty not found"}), 404
    faculty.name = data['name']
    faculty.dept = data['dept']
    faculty.phone = data['phone']
    faculty.email = data['email']
    db.session.commit()
    return jsonify({"message": "Faculty updated", "faculty": faculty.to_dict()})

@app.route('/delete-faculty', methods=['DELETE'])
def delete_faculty():
    id = request.get_json().get('id')
    faculty = Faculty.query.get(id)
    if not faculty:
        return jsonify({"message": "Faculty not found"}), 404
    db.session.delete(faculty)
    db.session.commit()
    return jsonify({"message": "Faculty deleted"})

# ------------------------- STUDENT ROUTES ------------------------- #
@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(**data)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added", "student": new_student.to_dict()}), 201

@app.route('/update-student', methods=['PUT'])
def update_student():
    data = request.get_json()
    student = Student.query.get(data.get('id'))
    if not student:
        return jsonify({"message": "Student not found"}), 404
    student.name = data['name']
    student.dept = data['dept']
    student.email = data['email']
    db.session.commit()
    return jsonify({"message": "Student updated", "student": student.to_dict()})

@app.route('/delete-student', methods=['DELETE'])
def delete_student():
    id = request.get_json().get('id')
    student = Student.query.get(id)
    if not student:
        return jsonify({"message": "Student not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted"})

if __name__ == '__main__':
    app.run(debug=True)
