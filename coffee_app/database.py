import sqlite3

CREATE_TABLE_BEAN = "CREATE TABLE IF NOT EXISTS Beans(id INTEGER PRIMARY KEY,name TEXT,method TEXT, rating INTEGER)";
INSERT_BEAN = "INSERT INTO Beans(name,method,rating) VALUES(?,?,?)"
GET_ALL_BEANS = "Select * FROM Beans"
GET_BEANS_BY_NAME = "Select * FROM Beans Where name='?' "
GET_BEST_PREPARATION_FOR_BEAN = """
Select * From Beans
Where name=?
ORDER BY rating DESC
LIMIT 1;"""


def connect():
    return sqlite3.connect('data.db')
def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE_BEAN)

def add_bean(connection,name,method,rating):
    with connection:
        connection.execute(INSERT_BEAN,(name,method,rating))

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()

def get_beans_by_name(connection,name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME,(name,)).fetchall()
    
def get_best_preparation_for_beans(connection,name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN,(name)).fetchone()
