import sqlite3
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
