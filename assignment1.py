import xml.etree.ElementTree as ET
import sqlite3

mydb=sqlite3.connect('assignmentdb.sqlite')
mycursor=mydb.cursor()
mycursor.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Album(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    );
    CREATE TABLE Genre(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT 
    );
    CREATE TABLE Track(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        length INTEGER,rating INTEGER,count INTEGER
    );


''')
fname=input('enter file name:')
item=ET.parse(fname)
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
    track_name=lookup(entry,'Name')
    artist=lookup(entry,'Artist')
    album=lookup(entry,'Album')
    genre_name=lookup(entry,'Genre')
    length=lookup(entry,'Total Time')
    rating=lookup(entry,'Rating')
    count=lookup(entry,'Play Count')
    if track_name is None or artist is None or album is None:
        continue
    print(track_name,artist,album,genre_name,length,rating,count)
    mycursor.execute('''INSERT OR IGNORE INTO Artist(name) VALUES(?)''',(artist,))
    mycursor.execute('''SELECT id FROM Artist WHERE name=?''',(artist,))
    artist_id=mycursor.fetchone()[0]
    mycursor.execute('''INSERT OR IGNORE INTO Album(artist_id,title) VALUES(?,?)''',(artist_id,album))
    mycursor.execute('''SELECT id FROM Album WHERE title=?''',(album,))
    album_id=mycursor.fetchone()[0]
    mycursor.execute('''INSERT  INTO Genre(name) VALUES(?)''',(genre_name,))
    mycursor.execute('''SELECT id FROM Genre WHERE name=?''',(genre_name,))
    genre_id=mycursor.fetchone()[0]
    mycursor.execute('''INSERT OR REPLACE INTO Track(title,album_id,genre_id,length,rating,count) VALUES(?,?,?,?,?,?) ''',(track_name,album_id,genre_id,length,rating,count))
    mydb.commit()