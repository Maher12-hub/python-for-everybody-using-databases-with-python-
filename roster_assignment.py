import json
import sqlite3
mydb=sqlite3.connect('assignmentdb.sqlite')
mycursor=mydb.cursor()
mycursor.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Course;
        DROP TABLE IF EXISTS Member;
        CREATE TABLE User(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        );
        CREATE TABLE Course(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE
        );
        CREATE TABLE Member(
            user_id INTEGER,
            course_id INTEGER,
            role INTEGER,
            PRIMARY KEY(user_id,course_id)
            );

''')
fname=input('enter a file name:')
data=open(fname).read()
json_data=json.loads(data)
for entry in json_data:
    name=entry[0]
    title=entry[1]
    role=entry[2]
    print(name,title,role)
    mycursor.execute('''INSERT OR IGNORE INTO User(name) VALUES(?)''',(name,))
    mycursor.execute('''SELECT id FROM User WHERE name=? ''',(name,))
    user_id=mycursor.fetchone()[0]
    mycursor.execute('''INSERT OR IGNORE INTO Course(title) VALUES(?)''',(title,))
    mycursor.execute('''SELECT id FROM Course WHERE title=? ''',(title,))
    course_id=mycursor.fetchone()[0]
    mycursor.execute('''INSERT OR REPLACE INTO Member(user_id,course_id,role) VALUES(?,?,?)''',(user_id,course_id,role))
    mydb.commit()
