import sqlite3
con = sqlite3.connect('connect.db')
print ('database connected')

#con.execute("INSERT INTO Employee VALUES (1,'daisy',28,15000)");
#con.execute("INSERT INTO Employee VALUES (2,'mai',30,25000)");
#con.execute("INSERT INTO Employee VALUES (3,'del',48,32000)");
#con.execute("INSERT INTO Employee VALUES (4,'alp',32,12000)");
con.execute("INSERT INTO Employee VALUES (5,'pale','25',15923)");
con.commit()
print('successfull')
con.close();