import psycopg2

_username = 'postgres'
_password = 'psql'
_db_name = 'postgres'
_host = 'localhost'

def _connect():
    connection_string = "user='{user}' password='{pw}' dbname='{db}' host='{host}'".format(user=_username, pw=_password, db=_db_name, host=_host)
    try:
        return psycopg2.connect(connection_string)
    except Exception as e:
        print('Connection Failed')
        print(e)
        return None

class BaseORM:
    ## TODO: parameterize this

    def __init__(self):
        class_name = self.__class__.__name__
        conn = _connect()
        if conn is not None:
            cur = conn.cursor()
            # cur.execute('CREATE TABLE IF NOT EXISTS {name} '.format(name=class_name))
            cur.close()
            conn.close()

class Types:
    ## constants
    SERIAL = 'SERIAL'
    INTEGER = 'INTEGER'