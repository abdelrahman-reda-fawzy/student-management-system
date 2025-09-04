import sqlite3
from db import get_connection

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
