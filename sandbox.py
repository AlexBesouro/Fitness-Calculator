import psycopg2
# connection = psycopg2.connect(host="localhost", port="5432", database="Food_db", user="postgres",password="postgres")

from config import config
def connect():
    # Connect to the DB
    connection = None
    crsr = None
    try:
        params = config(filename="database.ini", section="postgresql")
        print(params)
        print("Connecting to the postgreSQL database ...")
        connection = psycopg2.connect(**params)
        # print(connection)

        # Create a cursor
        crsr = connection.cursor()

        print("PostgreSQL database version: ")
        crsr.execute("SELECT version()")
        db_version = crsr.fetchone()
        print(db_version)


        # # Create table
        # create_table = ("CREATE TABLE IF NOT EXISTS customers ("
        #                 "customer_id SERIAL NOT NULL, "
        #                 "first_name VARCHAR(255) NOT NULL, "
        #                 "phone_number INT NOT NULL)")
        # crsr.execute(create_table)

        # # Insert values
        # insert_script = ("INSERT INTO customers (customer_id, first_name, phone_number) VALUES (6,'Aleks', 133232)")
        # # insert_values = (3, "Aleks", "Bes", "mail", 1232, 0)
        # crsr.execute(insert_script)

        # crsr.execute("SELECT * FROM customers")
        # column_names = [desc[0] for desc in crsr.description]
        # print(column_names)

        data = crsr.execute("SELECT max(customer_id) FROM customers")
        data = crsr.fetchall()[0][0]
        print(data)
        # for i in data:
        #     print(i[0])


        connection.commit()
        print("Commited")


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