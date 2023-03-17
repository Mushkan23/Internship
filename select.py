import sqlite3
con = sqlite3.connect('connect.db')
data = con.execute("Select * from Employee");
con.execute('UPDATE Employee SET Age = 54 WHERE Age <= 48')
for row in data:
    print ("ID = " ,row[0])
    print ("Name = " ,row[1])
    print ("Age = " ,row[2])
    print ("Salary = " , row[3],"\n")
con.close();
print("Successfull Done")
con.close();
