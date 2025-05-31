import psycopg2

def get_db_open_media():
        try:
            conn = psycopg2.connect("dbname='db_open_media' user='postgres' host='localhost' password='postgres'")
            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

conn = get_db_open_media()

print(conn)