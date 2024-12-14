from database_connect import connect_database

# 1. Task 2: Develop a function to add workout sessions to the 'WorkoutSessions' table for a specific member.

def add_workout_session():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            members_id = input("Enter the ID for the member who completed this workout session: ")
            
            query = "SELECT id FROM Members WHERE id = %s"
            cursor.execute(query, (members_id,)) 
            member = cursor.fetchone() 
            
            if not member: 
                print("Error: Member ID not found in the database.") 
                return
                                
            session_date = input("Enter the date this session was done (YYYY-MM-DD): ")
            session_duration = int(input("Enter the time this session took to complete:"))
            burned_calories = int(input("Enter the total calories burned for this session: "))
            session_id =  int(input("Please enter the session ID: "))

            new_workout_session = (members_id, session_date,session_duration, burned_calories, session_id)

            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned, session_id) VALUES (%s,%s, %s, %s, %s)"
            cursor.execute(query, new_workout_session)
            conn.commit()
            print(f"Workout session has been added to member with id: {members_id}")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# 1. Task 4: Create a function to delete a workout session based on session ID.

def delete_workout_session():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            workout_session_id = int(input("Enter the session id number: "))

            query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, (workout_session_id, ))
            session = cursor.fetchone()

            if session is not None:
                session = session[0]

                query = "DELETE FROM WorkoutSessions WHERE session_id = %s "

                # Attempting to delete session

                cursor.execute(query, (session, ))
                conn.commit()
                print("Workout Session has been removed.")

            else:
                print("Invalid Session ID")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()