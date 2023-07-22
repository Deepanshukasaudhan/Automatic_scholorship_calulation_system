import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import time
from functions import get_db_connection,guide_login,get_students,get_students_with_null_approval,getapproval,get_student,get_attendance,get_approval,change_approval,change_approval_rej,student_login,get_attendance_student,get_scholarship,getstatus,getcomments,reg_database,create_approval_entry

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


GID=""
SID=""

@app.route('/', methods=('GET', 'POST'))
def login():
    global SID
    if request.method == 'POST':
        emailid = request.form['email']
        pwd = request.form['password']
        print(emailid,pwd);
        if not emailid:
            flash('Enter E-Mail!')
        if not pwd:
            flash('Enter Password')
        else:
            conn = get_db_connection()
            actual_password = conn.execute('SELECT * FROM student WHERE email = ?',(emailid,)).fetchone()
            conn.commit()
            conn.close()
            if actual_password==None:
                flash('Invalid User')
            elif actual_password['password']!=pwd:
                return redirect(url_for('invalid_student'))
            else:
                SID=actual_password['email']
                return redirect(url_for('valid_student'))
    return render_template('student_login.html')

@app.route('/invalid_student')
def invalid_student():
    return render_template('student_new_invalid.html')

@app.route('/profile_student')
def valid_student():
    global SID
    temp=student_login(SID)
    return render_template('student_account.html', temp=temp)

@app.route('/attendance')
def student_attendance():
    global SID
    att=get_attendance_student(SID)
    totaldays=0
    presentdays=0
    for i in att:
        if i['status']=='Y':
            presentdays=presentdays+1
        totaldays=totaldays+1
    return render_template('student_new_view_att.html', att=att,presentdays=presentdays,totaldays=totaldays)

@app.route('/scholarship')
def show_scholarship():
    global SID
    sch=get_scholarship(SID)
    st=getstatus(SID)
    comment=getcomments(SID)
    prd=time.strftime("%Y-%m")
    return render_template('student_scholarship.html', sch=sch,st=st,comment=comment,prd=prd)


@app.route('/Registerst', methods=('GET', 'POST'))
def register():
    global SID
    if request.method == 'POST':
        n = request.form['name']
        em = request.form['email']
        p = request.form['password']
        d = request.form['date']
        pr = request.form['programme']
        yr = request.form['year']
        mb = request.form['mobile']
        gn = request.form['gender']
        gd = request.form['guide']
        rn=request.form['roll']
        if (not n) or (not em) or (not p) or (not d) or (not pr) or (not yr) or (not mb) or (not gn) or (not gd) or (not rn):
            flash('Enter all values!')
        elif gn!='M' and gn!='F':
            flash('Invalid Gender')
        elif yr<'1' or yr>'5':
            flash('Invalid Year')
        elif pr!='MTech' and pr!='PhD':
            flash("Invalid programme")
        else:
            reg_database(n,em,p,d,pr,yr,mb,gn,gd,rn)
            create_approval_entry(rn)
            flash("Successfully Registered")
            return redirect(url_for('login'))
    return render_template('student_register.html')


@app.route('/guide', methods=('GET', 'POST'))
def create():
    global GID
    if request.method == 'POST':
        emailid = request.form['email']
        pwd = request.form['password']
        print(emailid,pwd);
        if not emailid:
            flash('Enter E-Mail!')
        if not pwd:
            flash('Enter Password')
        else:
            conn = get_db_connection()
            actual_password = conn.execute('SELECT * FROM guide WHERE email = ?',(emailid,)).fetchone()
            conn.commit()
            conn.close()
            if actual_password==None:
                flash('Invalid User')
            elif actual_password['password']!=pwd:
                return redirect(url_for('invalid_guide'))
            else:
                GID=actual_password['email']
                return redirect(url_for('valid_guide'))
    return render_template('guide_new_guide_login.html')

@app.route('/invalid_guide')
def invalid_guide():
    return render_template('guide_new_invalid.html')

@app.route('/profile_guide')
def valid_guide():
    global GID
    temp=guide_login(GID)
    return render_template('guide_new_guideprofile.html', temp=temp)

@app.route('/view_attendance')
def view_attendance():
    global GID
    temp=guide_login(GID)
    temp2=get_students(temp['guideid'])
    return render_template('guide_selectstudents.html', temp=temp2)


@app.route('/approve_students', methods=('GET', 'POST'))
def approve_students():
    global GID
    temp=guide_login(GID)
    temp2=get_students_with_null_approval(temp['guideid'])
    return render_template('guide_new_selectstudents.html', temp=temp2)

@app.route('/view_attendance_roll/<roll_no>')
def getatt(roll_no):
    att = get_attendance(roll_no)
    totaldays=0
    presentdays=0
    for i in att:
        if i['status']=='Y':
            presentdays=presentdays+1
        totaldays=totaldays+1
    return render_template('guide_new_view_att.html', att=att,presentdays=presentdays,totaldays=totaldays)


@app.route('/approved/<roll_no>', methods=('GET', 'POST'))
def approved(roll_no):
    comm=''
    if request.method == 'POST':
        comm = request.form['comm']
        print(comm)
        change_approval(roll_no,comm)
        return redirect(url_for('approve_students'))
    return render_template('guide_new_get_comments.html')

@app.route('/rejected/<roll_no>', methods=('GET', 'POST'))
def rejected(roll_no):
    comm=''
    if request.method == 'POST':
        comm = request.form['comm']
        print(comm)
        change_approval_rej(roll_no,comm)
        return redirect(url_for('approve_students'))
    return render_template('guide_new_get_comments.html')
