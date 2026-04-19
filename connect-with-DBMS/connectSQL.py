import psycopg2
from config import config

def connect():
    
    conn = None
    
    try:
        # read connection parameters
        kwargs = config()
        # connect to the PostgreSQL server 
        conn = psycopg2.connect(**kwargs)
        print('connected successfully')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn