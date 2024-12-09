from member_functions import add_member, update_member_age
from workout_sessions_functions import add_workout_session, delete_workout_session
from advanced_analysis import get_members_in_age_range
from database_connect import connect_database
from mysql.connector import Error

def create_tables():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()


            sql = '''CREATE TABLE if not exists Members (
                id INT AUTO_INCREMENT,
                name VARCHAR(100),
                age INT,
                PRIMARY KEY (id)
            );'''

            cursor.execute(sql)

            sql1 = '''CREATE TABLE if not exists WorkoutSessions(
            member_id INT ,
            date DATE,
            duration_minutes INT,
            calories_burned INT,
            session_id INT AUTO_INCREMENT,
            PRIMARY KEY (session_id),
            FOREIGN KEY (member_id) REFERENCES Members(id) 
            );'''

            cursor.execute(sql1)
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
finally:
    conn.close()

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
                member_id = int
                member_name = input("Enter the member's name: ")
                member_age = int(input("Enter the member's age: "))
                add_member(member_id, member_name, member_age)
            elif user_option == 2:
                if not 'Members':
                    print("Members MUST be added to the database before a workout session can be added")
                else:
                    members_id = input("Enter the ID for the member who completed this workout session: ")
                    if members_id in 'Members':
                        session_date = input("Enter the date this session was done (YYYY-MM-DD): ")
                        session_duration = int(input("Enter the time this session took to complete:"))
                        burned_calories = int(input("Enter the total calories burned for this session: "))
                        session_id = int 
                        add_workout_session(members_id, session_date, session_duration, burned_calories, session_id)
            elif user_option == 3:
                id_for_member = int(input("Enter the ID of the member who's age needs updating: "))
                if id_for_member in 'Members':
                    updated_age = int(input("Enter the member's updated age: "))
                update_member_age(id_for_member, updated_age)
            elif user_option == 4:
                workout_session_id = input("Enter the session id number: ")
                if workout_session_id in 'WorkoutSessions':
                    delete_workout_session(workout_session_id)
            elif user_option == 5:
                    starting_age = int(input("Enter the age to start age range: "))
                    ending_age = int(input("Enter the age to end with: "))                
                    get_members_in_age_range(starting_age, ending_age)
            elif user_option == 6:
                print("Now Exiting. Thank you for choosing The Gym Database Management! Until next time....")
                break
                
            else:
                print("INVALID INPUT: Please try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()