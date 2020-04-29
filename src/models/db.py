import sqlite3

class BaseORM(): 
    TEXT = 'TEXT'
    REAL = 'REAL'
    ID = 'INTEGER PRIMARY KEY AUTOINCREMENT'
    INT = 'INT'

    @staticmethod
    def connect() -> sqlite3.Connection:
        return sqlite3.connect('src/models/atlas.db')
    
    @classmethod
    def create_table(cls, db_dict: dict, options: dict = None) -> None:
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
    
    @classmethod
    def from_dict(cls, d: dict):
        c = cls()
        for k in list(cls.__dict__['__annotations__']):
            if k in d:
                c.__setattr__(k, d[k])
        return c

    @classmethod
    def get(cls, filters: dict = None):
        conn = BaseORM.connect()
        cur = conn.cursor()
        q = 'SELECT * FROM {tbl} WHERE {flts};'.format(tbl=cls.__name__, flts=" AND ".join([ k + ' = ?' for k in filters.keys() ]))
        ret = None
        try:
            cur.execute(q, tuple(filters.values()))
            ret = cls()
            index = 0
            res = list(cur.fetchone())
            for k in list(cls.__dict__['__annotations__']):
                ret.__setattr__(k, res[index])
                index += 1
            return ret
        except Exception as e:
            print(e)
        finally:
            conn.close()
            return ret

    def insert(self) -> int:
        query = "INSERT INTO {tbl} ({keys}) VALUES ({vals});".format(
            tbl = self.__class__.__name__,
            keys = ", ".join(self.__dict__.keys()),
            vals = ", ".join([ '?' for k in self.__dict__.keys()])
        )
        conn = BaseORM.connect()
        cur = conn.cursor()
        ret = None
        try:
            cur.execute(query, tuple(self.__dict__.values()))
            for id in list(cur.execute('SELECT last_insert_rowid()').fetchone()):
                ret = id
            conn.commit()
        except Exception as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
            return ret
    
    @classmethod
    def delete(cls, filters: dict):
        query = "DELETE FROM {tbl} WHERE {flts};".format(tbl=cls.__name__, flts=" AND ".join([ k + " = ?" for k in filters.keys()]))
        conn = BaseORM.connect()
        cur = conn.cursor()
        ret = False
        try:
            cur.execute(query, tuple(filters.values()))
            conn.commit()
            ret = True
        except Exception as e:
            print(e)
            ret = False
        finally:
            conn.close()
            return ret