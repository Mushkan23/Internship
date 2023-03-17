import sqlite3
con = sqlite3.connect('connect.db')
data = con.execute("Select * from Employee");
con.execute('''DELETE from Employee WHERE ID=1 ''');
print('Successfull Done')
con.commit()
con.close()