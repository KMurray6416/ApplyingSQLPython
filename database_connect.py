import mysql.connector
from mysql.connector import Error

def connect_database():
    """Connect to the MySQL database and return the connection object"""

    db_name ="your database name"
    user = "your username"
    password = "your password"
    host = "database host"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        print("Connected to MySQL database successfully")
        return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None