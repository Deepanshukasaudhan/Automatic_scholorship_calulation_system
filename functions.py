import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import datetime

def reset_approval():
    current_time = datetime.datetime.now()
    if current_time.day==1 and current_time.hour==0:
        conn = get_db_connection()
        sql_update_query = """Update approval set status='null'"""
        conn.execute(sql_update_query)
        conn.commit()



def get_db_connection():
    conn = sqlite3.connect('database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def guide_login(email):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM guide WHERE email = ?',(email,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_students(gd):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM student WHERE guideid = ?',(gd,)).fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_students_with_null_approval(gd):
    conn = get_db_connection()
    post = conn.execute('SELECT student.rollno,student.name FROM student,approval WHERE guideid = ? AND student.rollno=approval.rollno AND approval.status="null"',(gd,)).fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post

def getapproval(roll):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM approval WHERE rollno = ?",(roll,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_student(roll):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM student WHERE rollno = ?',(roll,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_attendance(roll):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM attendance WHERE rollno = ?',(roll,)).fetchall()
    if post is None:
        print("Yes")
        abort(404)
    return post

def get_approval(roll):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM approval WHERE rollno = ?',(roll,)).fetchone()
    if post is None:
        abort(404)
    return post

def change_approval(roll,comm):
    conn = get_db_connection()
    sql_update_query = """Update approval set status = ?,comment=? where rollno = ?"""
    data = ('Y',comm,roll)
    conn.execute(sql_update_query, data)
    conn.commit()

def change_approval_rej(roll,comm):
    print("Uh oh rejected!")
    conn = get_db_connection()
    sql_update_query = """Update approval set status = ?,comment=? where rollno = ?"""
    data = ('N',comm,roll)
    conn.execute(sql_update_query, data)
    conn.commit()

def student_login(email):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM student WHERE email = ?',(email,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_attendance_student(email):
    conn = get_db_connection()
    temp = conn.execute('SELECT rollno FROM student WHERE email = ?',(email,)).fetchone()
    post = conn.execute('SELECT * FROM attendance WHERE rollno = ?',(temp['rollno'],)).fetchall()
    if post is None:
        abort(404)
    return post

def get_scholarship(email):
    conn = get_db_connection()
    temp = conn.execute('SELECT * FROM student WHERE email = ?',(email,)).fetchone()
    post = conn.execute('SELECT * FROM scholarship WHERE programme = ? AND year=?',(temp['programme'],temp['year'],)).fetchone()
    if post is None:
        abort(404)
    return post['stipend']

def getstatus(email):
    conn = get_db_connection()
    temp = conn.execute('SELECT rollno FROM student WHERE email = ?',(email,)).fetchone()
    post = conn.execute('SELECT * FROM approval WHERE rollno = ?',(temp['rollno'],)).fetchone()
    if post is None:
        abort(404)
    if post['status']=='null':
        return "Pending Approval"
    elif post['status']=="Y":
        return "Approved"
    elif post['status']=='N':
        return "Rejected"

def getcomments(email):
    conn = get_db_connection()
    temp = conn.execute('SELECT rollno FROM student WHERE email = ?',(email,)).fetchone()
    post = conn.execute('SELECT * FROM approval WHERE rollno = ?',(temp['rollno'],)).fetchone()
    if post is None:
        abort(404)
    return post['comment']


def reg_database(n,em,p,d,pr,yr,mb,gn,gd,rn):
    conn = get_db_connection()
    sql_update_query = "INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    data = (em,d,yr,pr,gn,rn,mb,p,n,gd)
    conn.execute(sql_update_query, data)
    conn.commit()


def create_approval_entry(rn):
    conn = get_db_connection()
    sql_update_query = "INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)"
    data = (rn,'null','New Registration')
    conn.execute(sql_update_query, data)
    conn.commit()
