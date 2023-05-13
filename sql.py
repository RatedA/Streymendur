import utility
import mysql.connector
from mysql.connector import Error

config = utility.openConfig()
host_name = config['sql']['host']
user_name = config['sql']['user']
user_password = config['sql']['psw']
db_name = config['sql']['dbname']

def sql_connect(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database = db_name

        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = sql_connect(host_name, user_name, user_password, db_name)

def create_sqldb(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def querydb(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def querymanydb(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#everything above is useful asf

#from user.json to sql table users
def user_jsonsql():
    userstupe = []
    data = utility.openUser()
    for u in data:
        #print(u,v['stream_id'])
        userstupe.append((data[u]['stream_id'], u))
    return userstupe
insert_users = "INSERT INTO users (userid, username) VALUES (%s, %s)"


#may sql function dudes
create_usertable = """
CREATE TABLE users(
    userid INT PRIMARY KEY,
    username VARCHAR(40) NOT NULL,
    firstseen DATE,
    lastseen DATE,
    tottimelive INT,
    islive BOOLEAN
);
    """

create_userlive = """
CREATE TABLE userslive(

    userid INT PRIMARY KEY,
    username VARCHAR(40) NOT NULL,
    timelive INT,
    tags VARCHAR(40)
);
"""

#make it create db, tables if not exist then serve as sql util file uwu