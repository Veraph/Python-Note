import unittest
from city_functions import city_country
class CityTest(unittest.TestCase):
    '''test city_functions.py'''
    def test_city_country(self):
        formatted_geo = city_country('Beijing', 'China')
        self.assertEqual(formatted_geo, 'Beijing, China')
    def test_city_country_population(self):
        formatted_geo = city_country('Beijing', 'China', 1000)
        self.assertEqual(formatted_geo, 'Beijing, China-population 1000')
        
unittest.main()