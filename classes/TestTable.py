from db.BaseORM import BaseORM, Types

class TestTable(BaseORM):
    id = ('id', Types.SERIAL)

    def _print(self):
        print(self.__class__.__name__)


if __name__ == '__main__':
    t = TestTable()
