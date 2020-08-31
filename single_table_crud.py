import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='users'
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE users")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE TABLE users (name VARCHAR(255),email VARCHAR(255))")
#mycursor.execute("INSERT INTO users VALUES('maher','maheribne12@gmail.com')")
#user_list=[('sunny','sunny@gmail.com'),('anha','anha@gmail.com'),('rahi','rahi@gmail.com')]
#mycursor.execute("INSERT INTO users VALUES('sunny','sunny@gmail.com')")
#mycursor.execute("INSERT INTO users VALUES('anha','anha@gmail.com')")
#mycursor.execute("INSERT INTO users VALUES('rahi','rahi@gmail.com')")
#mycursor.execute("DELETE FROM users WHERE name='anha'")
#mycursor.execute("UPDATE users SET name='mehanaz' WHERE email='sunny@gmail.com'")
mycursor.execute("SELECT * FROM users WHERE name='maher'")

#mydb.commit()
