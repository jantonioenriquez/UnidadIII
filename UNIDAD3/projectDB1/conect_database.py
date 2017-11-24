import psycopg2
from config import config

"""Name: Jose Antonio Enriquez Cabrera.
   Group: GITI9072."""
def connect():
    """Conect to postgrsql database server"""
    conn = None
    try:
        #read conection parameters
        params= config()

        #connect to the prosgresql server
        print("conecting to postgresql database...")
        conn = psycopg2.connect(**params)

        # create cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connectio closed.")

if __name__ == '__main__':
    connect()