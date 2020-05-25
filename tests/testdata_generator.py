def generate_valid_csv_addresses() -> list:
    """Generate valid addresses as an array matching the OpenAddress dataset schema

    Returns:
        list -- List of valid addresses
    """
    return [
        [-72.8980387, 41.327625, '1656', 'STATE ST', '0000', 'HAMDEN',None,None, '06514',None, '6070b4057f3431b7'],
        [-72.8967273, 41.3278167, '88', 'WELTON ST', '0000', 'HAMDEN',None,None, '06514',None, '4095584da0ed12b7'],
        [-72.8980698, 41.3277615, '1662', 'STATE ST' ,'0000', 'HAMDEN',None,None, '06514',None, '1db047ae91efa3eb'],
        [-72.8972739, 41.3277867, '1655', 'STATE ST', '0000', 'HAMDEN',None,None, '06514',None, '77813e6c3e8503a1'],
        [-72.896019, 41.3279622, '87', 'WELTON ST', '0000', 'HAMDEN',None,None, '06514',None, '7e9ca5f362e9e24f'],
        [-72.8981035, 41.3279135, '1668', 'STATE ST', '0000', 'HAMDEN',None,None, '06514',None, 'b3ea3c27581e518c']
    ]

def create_test_csv(file_name:str):
    """Create a testable csv file for parsing

    Contains the following rows:
        Row[0]: Header row ['LON', 'LAT', 'NUMBER', 'STREET', 'UNIT', 'CITY', 'DISTRICT', 'REGION', 'POSTCODE', 'ID', 'HASH']
        Row[1-6]: Valid data rows containing Lon, Lat, Number, Street, Unit, City, Postcode, Hash

    Arguments:
        file_name {str} -- Filename/path to be used for the demo file
    """
    import csv
    w = csv.writer(open(file_name, 'w'))
    rows = [
        ['LON', 'LAT', 'NUMBER', 'STREET', 'UNIT', 'CITY', 'DISTRICT', 'REGION', 'POSTCODE', 'ID', 'HASH']
    ]
    rows.extend(generate_valid_csv_addresses())
    w.writerows(rows)