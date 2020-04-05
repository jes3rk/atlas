import psycopg2

class BaseORM:
    ## TODO: parameterize this
    _username = 'postgres'
    _password = 'psql'
    _db_name = 'postgres'
    _host = 'localhost'

    def __init__(self):
        class_name = self.__class__.__name__
        conn = self._connect()
        if conn is not None:
            cur = conn.cursor()
            cur.close()
            conn.close()


    def _connect(self):
        try:
            connect_str = "dbname='{db}' user='{user}' password='{pw}' host='{host}'".format(db=self._db_name, user=self._username, pw=self._password, host=self._host)
            return psycopg2.connect(connect_str)
        except Exception as e:
            print('Connection failed')
            print(e)
            return None

class Types:
    ## constants
    SERIAL = 'SERIAL'
    INTEGER = 'INTEGER'