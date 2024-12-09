from database_connect import connect_database

# 1. Task 2: Develop a function to add workout sessions to the 'WorkoutSessions' table for a specific member.

def add_workout_session(member_id, date, duration_minutes, calories_burned, session_id):
    conn = connect_database()
    if conn is not None:
        try:
            if not 'Members':
                cursor = conn.cursor()

                new_workout_session = (member_id, date, duration_minutes, calories_burned, session_id)

                query = "INSERT INTO WorkoutSessions WHERE member_id = %s (date, duration_minutes, calories_burned, session_id) VALUES (%s, %s, %s, %s)"

                cursor.execute(query, new_workout_session)
                conn.commit()
                print(f"Workout session has been added to member with id: {member_id}")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# 1. Task 4: Create a function to delete a workout session based on session ID.

def delete_workout_session(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Checking if session exists

            session_check = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
            if session_check is not None:

                query = "DELETE FROM WorkoutSessions WHERE session_id = %s "

                # Attempting to delete session

                cursor.execute(query, session_id)
                conn.commit()
                print("Workout Session has been removed.")

            else:
                print("Invalid Session ID")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()