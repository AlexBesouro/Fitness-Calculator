import psycopg2
from config import config

def connect():
    # Connect to the DB
    connection = None
    crsr = None
    try:
        params = config(filename="food_database.ini", section="postgresql")
        print("Connecting to the postgreSQL database ...")
        connection = psycopg2.connect(**params)

        # Create a cursor
        crsr = connection.cursor()

        #Insert values
        insert_script = ("INSERT INTO food_calories (food_id, food_name, food_calories) VALUES (1, 'rice', 360)")

        crsr.execute(insert_script)
        connection.commit()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if crsr is not None:
            crsr.close()
        if connection is not None:
            connection.close()
            print("Database connection terminated.")





if __name__ == "__main__":
    connect()