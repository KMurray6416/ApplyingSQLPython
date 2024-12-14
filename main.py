from member_functions import add_member, update_member_age
from workout_sessions_functions import add_workout_session, delete_workout_session
from advanced_analysis import get_members_in_age_range
from database_connect import connect_database
from mysql.connector import Error

# Function to create the tables within database.

def create_tables():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Members table creation. Only executes if the table does not exist already.

            table_0_query = '''CREATE TABLE if NOT EXISTS Members (
                id INT AUTO_INCREMENT,
                name VARCHAR(100),
                age INT,
                PRIMARY KEY (id)
            );'''

            cursor.execute(table_0_query)

            # WorkoutSessions table creation. Also only executes if the table does not exist already.

            table_01_query = '''CREATE TABLE if NOT EXISTS WorkoutSessions(
            member_id INT ,
            date DATE,
            duration_minutes INT,
            calories_burned INT,
            session_id INT AUTO_INCREMENT,
            PRIMARY KEY (session_id),
            FOREIGN KEY (member_id) REFERENCES Members(id) 
            );'''

            cursor.execute(table_01_query)
            conn.commit()
            print("Tables successfully created for database")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

try:
    conn = connect_database()
    if conn:
        create_tables() 
    else:
        print("Failed to connect to database or create tables.")
except Error as e:
    print(f"Error: {e}")

# Function for user friendly interface

def main():
    while True:
        try:
            print('''
                Gym Database Management: 
                ~~~~~~~~~~~~~~~~~~~~~~~~~
                1. Add A New Member
                2. Add A Workout Session for a Member 
                3. Update Member's Age
                4. Delete Workout Session
                5. Search Members In Age Range
                6. Exit
                    ''')

            user_option = int(input("Enter the Number for the task you would like to perform: 1-6 "))

            if user_option == 1 :
                add_member()
            elif user_option == 2:
                add_workout_session()
            elif user_option == 3:
                update_member_age()
            elif user_option == 4:
                    delete_workout_session()
            elif user_option == 5:       
                    get_members_in_age_range()
            elif user_option == 6:
                print("Now Exiting. Thank you for choosing The Gym Database Manager! Until next time....")
                break
                
            else:
                print("INVALID INPUT: Please try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()