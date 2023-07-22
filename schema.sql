DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS approval;
DROP TABLE IF EXISTS scholarship;
DROP TABLE IF EXISTS guide;

create table student(
  email varchar(30),
  dob date,
  year char(1),
  programme varchar(10),
  gender char(1),
  rollno char(9) primary key,
  mobno char(10),
  password varchar(30),
  name varchar(30),
  guideid char(9),
  foreign key(guideid) references guide(guideid)
);

create table attendance(
  dt date,
  status char(1),
  rollno char(9),
  primary key(dt,rollno),
  foreign key(rollno) references student(rollno)
);

create table approval(
  rollno char(9) primary key,
  status char(1),
  comment varchar(50),
  foreign key(rollno) references student(rollno)

);

create table scholarship(
  year char(1),
  programme varchar(10),
  stipend integer
);

create table guide(
  guideid char(9) primary key,
  name varchar(30),
  password varchar(30),
  email varchar(30),
  mobno char(10),
  dept varchar(30)
);
