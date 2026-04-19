from connectSQL import connect
from read_queries import read_queries

if __name__ == '__main__':
    # start the connection
    conn = connect()
    if conn is not None:
        # read the queries
        read_queries(conn)
        # Commit the transaction
        conn.commit()
        # end the connection
        conn.close()
        print('Database connection closed.')