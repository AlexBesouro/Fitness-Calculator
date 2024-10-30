import psycopg2
from psql_connetion import psql_connection

def insert_values(food_name, food_calories):
    connection, crsr = psql_connection("food_database.ini", "postgresql")
    last_id_number = crsr.execute("SELECT max(food_id) FROM food_calories")
    last_id_number = crsr.fetchall()[0][0]
    insert_script = (f"INSERT INTO food_calories (food_id, food_name, food_calories)"
                     f" VALUES (%s, %s, %s)")
    inserted_values = (last_id_number + 1, food_name, food_calories)

    crsr.execute(insert_script, inserted_values)
    connection.commit()

    if crsr is not None:
        crsr.close()
    if connection is not None:
        connection.close()
        print("Database connection terminated.")

insert_values("beef 5%", 140)



