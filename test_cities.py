import unittest
from city_functions import city_function

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like Fort Worth work."""
        location = city_function('fort worth', 'usa')
        self.assertEqual(location, 'Fort Worth, Usa')

    def test_city_country_population(self):
        """Do cities like Fort Worth work with population"""
        location = city_function('fort worth', 'usa', 50000)
        self.assertEqual(location, 'Fort Worth, Usa - Population 500000')

if __name__ == '__main__':
     unittest.main()