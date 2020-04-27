import sqlite3

class BaseORM(): 
    TEXT = 'TEXT'
    REAL = 'REAL'
    ID = 'INT PRIMARY KEY'

    @staticmethod
    def connect() -> sqlite3.Connection:
        return sqlite3.connect('src/models/atlas.sqlite')
    
    @classmethod
    def create_table(cls, db_dict: dict, options: dict = None):
        if 'id' not in db_dict:
            db_dict.update({ 'id': BaseORM.ID })
        query = "CREATE TABLE IF NOT EXISTS {nme} (".format(nme=cls.__name__)
        items = db_dict.items()
        i = len(items)
        for k, v in items:
            query += '{k} {v}'.format(k=k, v=v)
            if i > 1:
                query += ', '
            else:
                query += ');'
            i = i - 1
        conn = BaseORM.connect()
        c = conn.cursor()
        c.execute(query)
        if options is not None:
            if 'indexes' in options:
                for idx in options['indexes']:
                    c.execute('CREATE INDEX IF NOT EXISTS {idx} on {tbl}({cols});'.format(idx=idx['name'], tbl=cls.__name__, cols="".join(idx['columns'])))
        conn.commit()
        conn.close()