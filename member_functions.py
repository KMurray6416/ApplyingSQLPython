from database_connect import connect_database

# 1. Task 1: Write a function to add new members to the 'Members' table in the gym's database.

def add_member(id, name, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_member = (id, name, age)

            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("Member has been successfully added to database")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# 1. Task 3: Implement a function to update the age of a member.

def update_member_age(member_id, new_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            member_id_check = "SELECT * FROM Members WHERE id = %s"

            # Checking if Member exists

            id = cursor.execute(member_id_check)
            if id is not None:

                update_info = (member_id, new_age)

                query = "UPDATE Members WHERE id = %s SET age = %s"
                
                # Attempting to update info

                cursor.execute(query, update_info)
                conn.commit()
                print(f"Member with id: {member_id} Age has successfully been updated to {new_age}")
            
            else:
                print(" Invalid ID. ")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()



