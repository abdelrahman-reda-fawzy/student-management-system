from db import get_connection

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def add_student(name, age, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return student_id

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    return True

def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def add_course(name, credits):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (name, credits) VALUES (?, ?)", (name, credits))
    conn.commit()
    course_id = cursor.lastrowid
    conn.close()
    return course_id

def enroll_student(student_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    conn.commit()
    enrollment_id = cursor.lastrowid
    conn.close()
    return enrollment_id

def get_students_in_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.id, s.name, s.age, s.email
        FROM students s
        JOIN enrollments e ON s.id = e.student_id
        WHERE e.course_id = ?
    """, (course_id,))
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def get_courses_for_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.id, c.name, c.credits
        FROM courses c
        JOIN enrollments e ON c.id = e.course_id
        WHERE e.student_id = ?
    """, (student_id,))
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows
