# Student Management System

A lightweight **Flask + SQLite REST API** for managing students, courses, and enrollments.  
This backend system provides CRUD operations for student and course records, along with enrollment tracking.

---

## Features

- Manage students (add, update, delete, view)
- Manage courses (create, list)
- Enroll students in courses
- View students in a course and courses of a student
- Persistent storage with **SQLite**
- Minimal dependencies (Flask only)

## Project Structure

### Project Structure

```
student_management_system/
├── app.py            # Flask API endpoints and server
├── models.py         # CRUD logic for students, courses, enrollments
├── db.py             # Database connection and setup
├── data/
│   └── students.db   # SQLite database file
```

## Requirements

- Python 3.12 or higher
- Flask (install with `pip install flask`)

## Usage

1. Clone or download this repository.
2. Install Flask:
   ```powershell
   pip install flask
   ```
3. Start the Flask server:
   ```powershell
   python app.py
   ```
4. The API will be available at `http://127.0.0.1:5000/`.
5. Use an API client (like Postman) or browser to interact with the endpoints.

## Database

- The database file is located at `data/students.db`.
- If the file does not exist, it will be created automatically on first run.

## API Endpoints

The application exposes several RESTful API endpoints using Flask:

### Students

- `GET /students` — Retrieve all students.
- `POST /students` — Add a new student. JSON body: `{ "name": str, "age": int, "email": str }`
- `DELETE /students/<student_id>` — Delete a student by ID.

### Courses

- `GET /courses` — Retrieve all courses.
- `POST /courses` — Add a new course. JSON body: `{ "name": str, "credits": int }`

### Enrollments

- `POST /enroll` — Enroll a student in a course. JSON body: `{ "student_id": int, "course_id": int }`
- `GET /courses/<course_id>/students` — List all students enrolled in a course.
- `GET /students/<student_id>/courses` — List all courses a student is enrolled in.
