import mysql.connector
from mysql.connector import Error

def connect_database():
    """Connect to the MySQL database and return the connection object"""

    db_name ="your database"
    user = "your user"
    password = "Yourpassword!"
    host = "your host"

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