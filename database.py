import sqlite3
con = sqlite3.connect('students.db')
print("Database connected")
# c.execute("create table student (Fname varchar(200),Lname varchar(200),Email varchar(200),password varchar(200),ma1 varchar(30),ma2 varchar(30),ma3 varchar(30),ma4 varchar(30))") #for creating table
# print('abc')
c = con.cursor()
c.execute("SELECT * FROM student ;")
while True:
    res = c.fetchall()
    for a in res:
        print(a)
con.close()