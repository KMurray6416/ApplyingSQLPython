# 2. task 1 SQL BETWEEN Usage

from database_connect import connect_database

def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            members = []

            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"

            age_range = (start_age, end_age)

            cursor.execute(query, age_range)
            for member in cursor.fetchall():
                members.append(member)

            # Verify there are results

            if not members:
                print("There are no members within selected age range.")

                # Display Results
            else:
                for member in members:
                    member_id, name, age = member
                    return(f"ID: {member_id}, Member Name: {name}, Age: {age}")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()