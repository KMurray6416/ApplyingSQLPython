from database_connect import connect_database

# 1. Task 1: Write a function to add new members to the 'Members' table in the gym's database.

def add_member():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            member_id = int(input("Please enter a new member ID: "))
            member_name = input("Enter the member's name: ")

            query = "SELECT * FROM Members WHERE id = %s AND name = %s"
            cursor.execute(query, (member_id, member_name)) 
            member = cursor.fetchone()             
            
            if member:
                print("Error! This Member name with this ID already exists in database.")
                return 
            
            member_age = int(input("Enter the member's age: "))

            new_member = (member_id, member_name, member_age) 

            #print(f"Types: id={type(id)}, name={type(name)}, age={type(age)}")

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

def update_member_age():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            id_for_member = int(input("Enter the ID of the member who's age needs updating: "))

            query = "SELECT * FROM Members WHERE id = %s"

            cursor.execute(query, (id_for_member, ))
            id = cursor.fetchone()

            if id is not None:
                id = id[0]

                updated_age = int(input("Enter the member's updated age: "))

                query = "UPDATE Members SET age = %s WHERE id = %s"
                
                # Attempting to update info

                cursor.execute(query, (updated_age, id))
                conn.commit()
                print(f"Member with id: {id} Age has successfully been updated to {updated_age}")
            
            else:
                print(" Invalid ID. ")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()



