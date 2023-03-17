import sqlite3
con = sqlite3.connect('connect.db')
data = con.execute("Select * from Employee");
con.execute('''UPDATE Employee SET Name = 'met' WHERE Name = 'daisy' ''');
print('Successfull Done')
con.commit()
con.close()