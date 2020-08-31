import sqlite3
import json
import codecs
import webbrowser as wb
mydb=sqlite3.connect('geoload_assignment.sqlite')
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM Location')
fhand=codecs.open('where.js','w',"utf-8")
fhand.write('mydata=[\n')
count=0
for row in mycursor:
    data=str(row[1].decode())
    try:
        js=json.loads(str(data))
    except:
        continue
    if not('status' in js and js['status'] == 'OK') : 
        continue
    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    if lat==0 or lng==0:
        continue
    where=js["results"][0]["formatted_address"]
    where=where.replace("'","")
    try:
        print(where,lat,lng)
        count=count+1
        if count>1:
            fhand.write(',\n')
        output='['+str(lat)+','+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue
fhand.write("\n];\n")
mycursor.close()
fhand.close()
print(count,'records written to where_practice.js')
print('open where.html to view the data in a browser.')
wb.open('where.html')