import unittest
from src.loader.mun import Mun

class test_mun(unittest.TestCase):
    
    def test_parse_mun_name(self):
        options = [
            'city_of_mount_st_mary.csv',
            'vienna.csv',
            'town_of_apocolypse.csv',
            'eau_claire.csv',
            'new_york_city.csv'
        ]
        valid = [
            'Mount St Mary',
            'Vienna',
            'Apocolypse',
            'Eau Claire',
            'New York City'
        ]
        index = 0
        while index < len(options):
            self.assertEquals(valid[index], Mun.parse_mun_name(options[index]))
            index += 1

    def test_create_mun(self):
        file_path = 'data/us/ma/city_of_boston.csv'
        m = Mun(file_path)
        self.assertEquals(m.state, 'MA')
        self.assertEquals(m.mun_name, 'Boston')

if __name__ == "__main__":
    unittest.main()