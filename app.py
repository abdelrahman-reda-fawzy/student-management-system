from flask import Flask, request, jsonify
from db import setup_database, get_connection
from students import get_all_students, add_student, delete_student
from courses import get_all_courses, add_course
from enrollments import enroll_student, get_students_in_course, get_courses_for_student

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(get_all_students())

@app.route("/students", methods=["POST"])
def add_student_route():
    data = request.get_json()
    student_id = add_student(data["name"], data["age"], data["email"])
    return jsonify({"id": student_id, **data}), 201

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student_route(student_id):
    delete_student(student_id)
    return jsonify({"message": "Student deleted"}), 200

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(get_all_courses())

@app.route("/courses", methods=["POST"])
def add_course_route():
    data = request.get_json()
    course_id = add_course(data["name"], data["credits"])
    return jsonify({"id": course_id, **data}), 201

@app.route("/enroll", methods=["POST"])
def enroll_student_route():
    data = request.get_json()
    enrollment_id = enroll_student(data["student_id"], data["course_id"])
    return jsonify({"id": enrollment_id, **data}), 201

@app.route("/courses/<int:course_id>/students", methods=["GET"])
def students_in_course_route(course_id):
    return jsonify(get_students_in_course(course_id))

@app.route("/students/<int:student_id>/courses", methods=["GET"])
def courses_for_student_route(student_id):
    return jsonify(get_courses_for_student(student_id))

if __name__ == "__main__":
    setup_database()
    app.run(debug=True)
