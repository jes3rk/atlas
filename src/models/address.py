from src.models.db import BaseORM

class address(BaseORM):
    housenumber: str
    street: str
    city: str
    state: str
    zipcode: str
    latitude: float
    longitude: float
    id: int

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