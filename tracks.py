#import requests
#res=requests.get('https://www.py4e.com/code3/tracks/Library.xml')
#with open('library.xml','w',encoding=res.encoding) as wf:
#    wf.write(res.text)
import xml.etree.ElementTree as et
import sqlite3
mydb=sqlite3.connect('trackdb.sqlite')
mycursor=mydb.cursor()
mycursor.executescript('''
     DROP TABLE IF EXISTs Artist;
     DROP TABLE IF EXISTs Album;
     DROP TABLE IF EXISTs Track;
     CREATE TABLE Artist(
         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT UNIQUE
     );
     CREATE TABLE Album (
         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         artist_id INTEGER,
         title TEXT UNIQUE
     );
     CREATE TABLE Track(
         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         title TEXT UNIQUE,
         album_id INTEGER,
         length INTEGER,rating INTEGER,count INTEGER
     );
''')
fname=input('enter file name:')
item=et.parse(fname)
all=item.findall('dict/dict/dict')
def lookup(d,key):
    found=False
    for child in d:
        if found:
            return child.text
        if child.tag=='key' and child.text==key:
            found=True
    return None
for entry in all:
    if (lookup(entry,'Track ID') is None):
        continue
    name=lookup(entry,'Name')
    artist=lookup(entry,'Artist')
    album=lookup(entry,'Album')
    count=lookup(entry,'play count')
    rating=lookup(entry,'Rating')
    length=lookup(entry,'Total Time')
    if name is None or artist is None or album is None:
        continue
    print(name,artist,album,count,rating,length)
    mycursor.execute('''INSERT OR IGNORE  INTO Artist(name) VALUES(?)''',(artist,))
    mycursor.execute('''SELECT id FROM Artist WHERE name=?''',(artist,))
    artist_id=mycursor.fetchone()[0]
    mycursor.execute('''INSERT OR IGNORE INTO Album(artist_id,title) VALUES(?,?)''',(artist_id,album))
    mycursor.execute('''SELECT id FROM Album WHERE title=? ''',(album,))
    album_id=mycursor.fetchone()[0]
    mycursor.execute('''INSERT OR REPLACE INTO Track(title,album_id,length,rating,count) VALUES(?,?,?,?,?)''',(name,album_id,length,rating,count))
    mydb.commit()
