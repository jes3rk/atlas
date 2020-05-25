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
    def from_csv(raw: List[str], state: str, city: str = None):
        a = address()
        a.is_valid = False
        a.state = state
        if len(raw) == 11:
            valid_count = 0
            if _is_decimal(raw[0]):
                a.longitude = float(raw[0])
                valid_count += 1
                
            if _is_decimal(raw[1]):
                a.latitude = float(raw[0])
                valid_count += 1

            if _is_not_blank(raw[2]):
                a.housenumber = raw[2]
                valid_count += 1

            if _is_not_blank(raw[3]):
                a.street = raw[3]
                valid_count += 1

            if _is_not_blank(raw[5]):
                a.city = raw[5]
                valid_count += 1
            elif city is not None:
                a.city = city
                valid_count += 1

            if _is_valid_zip(raw[8]):
                a.zipcode = raw[8]
                valid_count += 1

            if valid_count == 6:
                a.is_valid = True
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
    if _is_not_blank(input):
        try:
            float(input)
            return True
        except ValueError:
            return False
    else:
        return False

def _is_valid_zip(input: str) -> bool:
    """Checks if given input is a valid zip code according to USPS zip code guidelines

    Input must be either:
        a) A string of numerical characters of length 5
        b) A string of 5 numercial characters followed by a dash followed by a string of 4 numerical characters

    Arguments:
        input {str} -- Variable to check

    Returns:
        bool -- Returns if is a valid zip code
    """
    if _is_not_blank(input) and type(input) is str and (len(input) == 5 or len(input) == 10):
        spliter = input.split('-')
        if len(spliter) <= 2:
            if len(spliter[0]) == 5:
                try:
                    int(spliter[0])
                except ValueError:
                    return False
            else:
                return False
            if len(spliter) > 1:
                if len(spliter[1]) == 4:
                    try:
                        int(spliter[1])
                    except ValueError:
                        return False
                else:
                    return False
            return True
        else:
            return False
    else:
        return False

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