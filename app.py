
from flask import Flask, request, jsonify
from db import setup_database
import models

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(models.get_all_students())

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    student_id = models.add_student(data["name"], data["age"], data["email"])
    return jsonify({"id": student_id, **data}), 201

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    models.delete_student(student_id)
    return jsonify({"message": "Student deleted"}), 200

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(models.get_all_courses())

@app.route("/courses", methods=["POST"])
def add_course():
    data = request.get_json()
    course_id = models.add_course(data["name"], data["credits"])
    return jsonify({"id": course_id, **data}), 201

@app.route("/enroll", methods=["POST"])
def enroll_student():
    data = request.get_json()
    enrollment_id = models.enroll_student(data["student_id"], data["course_id"])
    return jsonify({"id": enrollment_id, **data}), 201

@app.route("/courses/<int:course_id>/students", methods=["GET"])
def students_in_course(course_id):
    return jsonify(models.get_students_in_course(course_id))

@app.route("/students/<int:student_id>/courses", methods=["GET"])
def courses_for_student(student_id):
    return jsonify(models.get_courses_for_student(student_id))

if __name__ == "__main__":
    setup_database()
    app.run(debug=True)
