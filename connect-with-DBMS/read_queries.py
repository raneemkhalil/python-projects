from get_values_to_insert import get_values_to_insert


def get_queries(file_name='database.sql'):

    # read the sql file
    file = open(file_name, 'r')
    sql_file = file.read()
    file.close()
    # sort into an array
    queries = sql_file.replace('\n', '').split(';')
    return queries

def read_queries(conn):
    # create a cursor and connect to the current database
    cur = conn.cursor()
    # get the sql statement from the sql file
    queries = get_queries()
    for query in queries:
        # execute a statement(query)
        if query.startswith('INSERT INTO'):
            values = get_values_to_insert()
            query = query + ' ' + values
        if query.strip():
            cur.execute(query)
            print(query)

    # print the result of executed statement
    try:
        print(cur.fetchall())
    except Exception as err:
        print(err)
    # close the curser
    cur.close()