import psycopg2
from config import config

def psql_connection(filename, section):
    try:
        params = config(filename=filename, section=section)
        print("Connecting to the postgreSQL database ...")
        connection = psycopg2.connect(**params)

        # Create a cursor
        crsr = connection.cursor()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    return connection, crsr

# psql_connection("database.ini", "postgresql")

if __name__ == "__main__":
    psql_connection("database.ini", "postgresql")