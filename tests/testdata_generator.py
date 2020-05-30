def generate_csv_addresses(length: int, stringify=False, lon=False, lat=False, number=False, street=False, city=False, postcode=False) -> list:
    """Generate an array of addresses based on the OpenAddress schema to be used for generating random, non-real addresses.

    Can be used to generate valid looking addresses or invalid looking addresses.

    Arguments:
        length {int} -- Number of addresses to be returned

    Keyword Arguments:
        stringify {bool} -- If True will return addresses as an list of strings rather than the actual types. Useful for simulating raw CSV parsing (default: {False})
        lon {bool} -- Toggle for returning an invalid longitude value (default: {False})
        lat {bool} -- Toggle for returning an invalid latitude value (default: {False})
        number {bool} -- Toggle for returning an invalid housenumber value (default: {False})
        street {bool} -- Toggle for returning an invalid street value (default: {False})
        city {bool} -- Toggle for returning an invalid city value (default: {False})
        postcode {bool} -- Toggle for returning an invalid postcode (default: {False})

    Raises:
        TypeError: Input parameters don't match their perscribed types

    Returns:
        list -- List of addresses matching the OpenAddress schema
    """
    _types = [
        {
            'vars': [length],
            'type': int
        }, {
            'vars': [stringify, lon, lat, number, street, city, postcode],
            'type': bool
        }
    ]
    if not _type_check(_types):
        raise TypeError('Invalid Input Value')
    import random
    ret = list()
    while len(ret) < length:
        local = list()
        if lon: # 0
            local.append(random.choice([
                None,
                'apacadie'
            ]))
        else:
            local.append(random.uniform(-180, 180))
        if lat: # 1
            local.append(random.choice([
                None,
                'akjdfjkalkjsld'
            ]))
        else:
            local.append(random.uniform(-180, 180))
        if number: # 2
            local.append(None)
        else:
            local.append(str(random.randint(1, 10000)))
        if street: # 3
            local.append(None)
        else:
            local.append(random.choice([
                'STATE ST',
                'WATER ST', 
                'STADIUM RD',
                'RT 123',
                'WASHINGTON BLVD',
                'ELECTRIC AVENUE',
                'ABBEY RD', 
                'FIRST ST',
                'FIRST RD',
                'SECOND ST',
                'SECOND RD',
                'THIRD ST',
                'THIRD RD'
            ]))
        local.append('00000') # 4 this is for UNIT
        if city: # 5
            local.append(None)
        else:
            local.append(random.choice([
                'SPRINGFIELD',
                'ARLINGTON', 
                'NEW YORK CITY',
                'MANCHESTER',
                'BOSTON',
                'VIENNA',
                'AKRON',
                'HAMTON'
            ]))
        local.append(None) # 6 this is for DISTRICT
        local.append(None) # 7 this is for REGION
        if postcode: # 8
            local.append(random.choice([
                'asdfsdlalksldas',
                'ldkdjc',
                '1',
                '1234',
                21345,
                '12345-203a',
                '12393.1234',
                'asdfg-wkwe'
            ]))
        else:
            num = str(random.randint(1, 99999))
            while len(num) < 5:
                num = "0{n}".format(n=num)
            if random.random() > .5:
                num = "{n}-0192".format(n=num)
            local.append(num)
        local.append(None) # 9 this is for ID
        local.append(None) # 10 this is for HASH
        if stringify:
            index = 0
            for s in local:
                if s is not None:
                    local[index] = str(s)
                index += 1
        ret.append(local)
    return ret

def create_test_csv(file_name:str, data=None):
    """Create a testable csv file for parsing

    Contains the following rows:
        Row[0]: Header row ['LON', 'LAT', 'NUMBER', 'STREET', 'UNIT', 'CITY', 'DISTRICT', 'REGION', 'POSTCODE', 'ID', 'HASH']
        Row[1-6]: Valid data rows containing Lon, Lat, Number, Street, Unit, City, Postcode, Hash

    Arguments:
        file_name {str} -- Filename/path to be used for the demo file
        data {list} -- List of data to be used in the csv. Defaults to a list of valid addresses of length 1000
    """
    import csv
    w = csv.writer(open(file_name, 'w'))
    rows = [
        ['LON', 'LAT', 'NUMBER', 'STREET', 'UNIT', 'CITY', 'DISTRICT', 'REGION', 'POSTCODE', 'ID', 'HASH']
    ]
    if data is None:
        rows.extend(generate_csv_addresses(1000))
    else:
        rows.extend(data)
    w.writerows(rows)

def _type_check(to_validate: list) -> bool:
    """Check types of values.

    Arguments:
        to_validate {list} -- List of inputs to check. Format is a list of object 
        {
            'vars': [list, of, vars, to, check], 
            'type': type to compare against
        }

    Raises:
        TypeError: Input doesn't match the perscribed pattern

    Returns:
        bool -- True if all values passed in match their associated types
    """
    if type(to_validate) is list:
        for t in to_validate:
            try:
                for v in t['vars']:
                    if type(v) is not t['type']:
                        return False
            except:
                raise TypeError('Invalid Input Parameters')
        return True
    else:
        raise TypeError('Invalid Input Parameters')