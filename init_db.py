import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO guide (guideid, name, password, email, mobno, dept) VALUES (?, ?, ?, ?, ?, ?)",
            ('000000001', 'guide1','password','guide1@nitc','9999999991','dept1')
            )
cur.execute("INSERT INTO guide (guideid, name, password, email, mobno, dept) VALUES (?, ?, ?, ?, ?, ?)",
            ('000000002', 'guide2','password','guide2@nitc','9999999992','dept2')
            )
cur.execute("INSERT INTO guide (guideid, name, password, email, mobno, dept) VALUES (?, ?, ?, ?, ?, ?)",
            ('000000003', 'guide3','password','guide3@nitc','9999999993','dept1')
            )
cur.execute("INSERT INTO guide (guideid, name, password, email, mobno, dept) VALUES (?, ?, ?, ?, ?, ?)",
            ('000000004', 'guide4','password','guide4@nitc','9999999994','dept2')
            )
cur.execute("INSERT INTO guide (guideid, name, password, email, mobno, dept) VALUES (?, ?, ?, ?, ?, ?)",
            ('000000005', 'guide5','password','guide5@nitc','9999999995','dept1')
            )
cur.execute("INSERT INTO guide (guideid, name, password, email, mobno, dept) VALUES (?, ?, ?, ?, ?, ?)",
            ('000000006', 'guide6','password','guide6@nitc','9999999996','dept2')
            )
cur.execute("INSERT INTO guide (guideid, name, password, email, mobno, dept) VALUES (?, ?, ?, ?, ?, ?)",
            ('000000007', 'guide7','password','guide7@nitc','9999999997','dept1')
            )
cur.execute("INSERT INTO guide (guideid, name, password, email, mobno, dept) VALUES (?, ?, ?, ?, ?, ?)",
            ('000000008', 'guide8','password','guide8@nitc','9999999998','dept2')
            )

cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student1@nitc', '2001-05-18','2','MTech','M','M00000001','9999999901','password','Student 1','000000001')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student2@nitc', '2001-05-18','2','MTech','M','M00000002','9999999902','password','Student 2','000000001')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student3@nitc', '2001-05-18','1','MTech','M','M00000003','9999999903','password','Student 3','000000002')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student4@nitc', '2001-05-18','2','MTech','F','M00000004','9999999904','password','Student 4','000000003')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student5@nitc', '2001-05-18','2','MTech','M','M00000005','9999999905','password','Student 5','000000005')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student6@nitc', '2001-05-18','1','PhD','M','P00000001','9999999906','password','Student 6','000000005')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student7@nitc', '2001-05-18','3','PhD','F','P00000002','9999999907','password','Student 7','000000005')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student8@nitc', '2001-05-18','4','PhD','M','P00000003','9999999908','password','Student 8','000000007')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student9@nitc', '2001-05-18','1','PhD','M','P00000004','9999999909','password','Student 9','000000007')
            )
cur.execute("INSERT INTO student (email, dob, year, programme, gender, rollno, mobno, password, name, guideid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('student10@nitc', '2001-05-18','2','PhD','F','P00000005','9999999910','password','Student 10','000000008')
            )


cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('M00000001', 'null','Test Student')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('M00000002', 'null','Not Approved')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('M00000003', 'null','Not Approved')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('M00000004', 'null','Not Approved')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('M00000005', 'null','Not Approved')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('P00000001', 'null','Not Approved')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('P00000002', 'null','Not Approved')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('P00000003', 'null','Not Approved')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('P00000004', 'null','Not Approved')
            )
cur.execute("INSERT INTO approval (rollno, status, comment) VALUES (?, ?, ?)",
            ('P00000005', 'null','Not Approved')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','M00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','M00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','M00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','M00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','M00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','M00000001')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','M00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','M00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','M00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','M00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','M00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','M00000002')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','M00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','M00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','M00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','M00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','M00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','M00000003')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'N','M00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','M00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','M00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'N','M00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','M00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','M00000004')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','M00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','M00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','M00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','M00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','M00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','M00000005')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','P00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','P00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','P00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','P00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','P00000001')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','P00000001')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','P00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','P00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','P00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','P00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','P00000002')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','P00000002')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','P00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','P00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','P00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','P00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','P00000003')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','P00000003')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','P00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','P00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','P00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','P00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','P00000004')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','P00000004')
            )

cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-01', 'Y','P00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-02', 'Y','P00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-03', 'Y','P00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-04', 'Y','P00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-05', 'Y','P00000005')
            )
cur.execute("INSERT INTO attendance (dt, status, rollno) VALUES (?, ?, ?)",
            ('2022-11-06', 'Y','P00000005')
            )

cur.execute("INSERT INTO scholarship (year, programme, stipend) VALUES (?, ?, ?)",
            ('1', 'MTech',12000)
            )
cur.execute("INSERT INTO scholarship (year, programme, stipend) VALUES (?, ?, ?)",
            ('2', 'MTech',12000)
            )
cur.execute("INSERT INTO scholarship (year, programme, stipend) VALUES (?, ?, ?)",
            ('1', 'PhD',25000)
            )
cur.execute("INSERT INTO scholarship (year, programme, stipend) VALUES (?, ?, ?)",
            ('2', 'PhD',25000)
            )
cur.execute("INSERT INTO scholarship (year, programme, stipend) VALUES (?, ?, ?)",
            ('3', 'PhD',32000)
            )
cur.execute("INSERT INTO scholarship (year, programme, stipend) VALUES (?, ?, ?)",
            ('4', 'PhD',32000)
            )
cur.execute("INSERT INTO scholarship (year, programme, stipend) VALUES (?, ?, ?)",
            ('5', 'PhD',32000)
            )

connection.commit()
connection.close()
