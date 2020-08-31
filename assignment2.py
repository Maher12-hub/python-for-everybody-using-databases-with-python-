import sqlite3
mydb=sqlite3.connect('assignment2.sqlite')
mycursor=mydb.cursor()
mycursor.execute("DROP TABLE counts")
mycursor.execute("CREATE TABLE counts(org TEXT, count INTEGER)")
fname=input('enter file name:')
fo=open(fname)
for line in fo:
    if  line.startswith('From: '):
        a=line.split()[1]
        org=a.split('@')[1]
        mycursor.execute("SELECT count FROM counts WHERE org=?",(org,))
        data=mycursor.fetchone()
        if data is None:
            mycursor.execute("INSERT INTO counts VALUES(?,1)",(org,))
        else:
            mycursor.execute("UPDATE counts SET count= count+1 WHERE org=?",(org,) )
    mydb.commit()
        
mycursor.execute("SELECT org,count FROM counts ORDER BY count DESC")
myresult=mycursor.fetchall()
for result in myresult:
    print(str(result[0]),result[1])