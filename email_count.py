import sqlite3
mydb=sqlite3.connect('email.db')
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE counts(email TEXT, count INTEGER)")
fname=input('enter a filename:')
fo=open(fname)
for line in fo:
    if not line.startswith('From: '):
        continue
    pieces=line.split()
    email=pieces[1]
    mycursor.execute("SELECT count FROM counts WHERE email= ?",(email,))
    data=mycursor.fetchone()
    if data is None:
        mycursor.execute("INSERT INTO counts VALUES(?,1)",(email,))
    else:
        mycursor.execute("UPDATE counts SET count=count+1 WHERE email=?",(email,))
    mydb.commit()
mycursor.execute("SELECT email,count FROM counts ORDER BY count ")
myresult=mycursor.fetchall()
for result in myresult:
    print(result)