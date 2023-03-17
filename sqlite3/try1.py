import sqlite3
con = sqlite3.connect('try1.db')
#con.execute('CREATE TABLE try1(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, score INTEGER, grade VARCHAR)')
#con.execute("INSERT INTO try1(name,age,score,grade) VALUES('rai',21,123,'C'),('sayi',23,210,'B'),('diya',29,320,'A'),('deep',32,410,'A')");
for row in con.execute("SELECT age,score FROM try1 ORDER BY age DESC"):
    print(row)
con.commit()
print('successfull done.')
con.close()