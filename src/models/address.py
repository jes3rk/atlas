from src.models.db import BaseORM
from typing import List

class address(BaseORM):
    housenumber: str
    street: str
    city: str
    state: str
    zipcode: str
    latitude: float
    longitude: float
    id: int
    is_valid: bool

    @staticmethod
    def from_csv(raw: List[str]):
        a = address()
        a.is_valid = False
        index = 0
        vld_chk = True
        while vld_chk:
            if index >= len(raw):
                vld_chk = False
                break
            s = raw[index]
            if index == 0:
                if _is_decimal(s):
                    a.latitude = float(s)
                else:
                    vld_chk = False
            elif index == 1:
                if _is_decimal(s):
                    a.longitude = float(s)
                else:
                    vld_chk = False
            elif index == 2:
                if _is_not_blank(s):
                    a.housenumber = s
                else:
                    vld_chk = False
            elif index == 3:
                if _is_not_blank(s):
                    a.street = s
            index += 1
        return a

def _is_not_blank(input: str) -> bool:
    """Checks if the given input is not None and not blank

    Arguments:
        input {str} -- Variable to check

    Returns:
        bool -- Returns true if input is not None and not blank
    """
    return input is not None and input != ""    

def _is_decimal(input: str) -> bool:
    """Checks if given input is a valid decimal

    Arguments:
        input {str} -- Variable to check

    Returns:
        bool -- Returns true if input is not None, not blank, and is a decimal or integer
    """
    return _is_not_blank(input) and input.isdecimal()

address.create_table({
    'housenumber': BaseORM.TEXT,
    'street': BaseORM.TEXT,
    'city': BaseORM.TEXT,
    'state': BaseORM.TEXT,
    'zipcode': BaseORM.TEXT,
    'latitude': BaseORM.REAL,
    'longitude': BaseORM.REAL
}, {
    'indexes': [{
        'name': 'idx_address_city',
        'columns': ['city']
    }, {
        'name': 'idx_address_state',
        'columns': ['state']
    }, {
        'name': 'idx_address_zipcode',
        'columns': ['zipcode']
    }]
})