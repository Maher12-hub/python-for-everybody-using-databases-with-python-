import sqlite3
mydb=sqlite3.connect('words.db')
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE words(word TEXT, count INTEGER)")
fname=input('enter a filename:')
fo=open(fname)
for line in fo:
    word_list=line.split()
    for word in word_list:
        mycursor.execute("SELECT count FROM words WHERE word=?",(word,))
        data=mycursor.fetchone()
        if data is None:
            mycursor.execute("INSERT INTO words VALUES(?,1)",(word,))
        else:
            mycursor.execute("UPDATE words SET count=count+1 WHERE word=? ",(word,))
    mydb.commit()
mycursor.execute("SELECT word,count FROM words ORDER BY count DESC")
myresult=mycursor.fetchall()
for result in myresult:
    print(result)
