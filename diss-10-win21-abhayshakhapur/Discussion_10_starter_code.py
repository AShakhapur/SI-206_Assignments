import requests
import json
import unittest

# DEMO
def get_population(country_code, date):
    """
    This function takes a country code (e.g USA, BRA) and a date in years (e.g. 2017).
    Call the World Bank API to get population data searched by country and years.
    It returns the value as an integer.
    """
    url = "http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json"
    search = requests.get(url, )
    

def get_data(country_code, first_year, second_year):
    """
    This function takes a country code (e.g. USA, BRA) and two consecutive years (e.g. 2004 and 2005).
    Call the World Bank API to get population data searched by country and years.
    Return the data from API after converting to a python list
    that has population related information.
    Once you receive data from the API, paste the data to 
    JSON Online Editor and look at the contents.
    """
    pass

def population_growth(country_code, first_year, second_year):
    """
    This function receives three parameters: one is the country code and the other two
    are the two consecutive years that you want to find the population growth for.
    Call get_data and analyze the returned list.
    This function returns the population growths of the two years of the country in a tuple.
    """
    pass

class TestDiscussion10(unittest.TestCase):
    def test_get_population(self):
        data = get_population("USA", 2017)
        self.assertEqual(type(data), int)

        self.assertEqual(data, 324985539)
    def test_check_data(self):
        data1 = get_data('BRA', 2000, 2001)
        self.assertEqual(type(data1), type([]))
        self.assertEqual(data1[0]['page'], 1)
        self.assertEqual(data1[1][0]['countryiso3code'], "BRA")

    def test_population_growth(self):
        self.assertEqual(type(population_growth('CAN', 1998, 1999)), tuple)
        self.assertEqual(population_growth('USA', 2005, 2006), (0.921713167161207, 0.964253917136075))

def main():
    print("-----Population-----")
    year = 2017
    pop = get_population("USA", year)
    print("The total population in {} is {} in the year {}".format("USA", pop, year))
    print("-----Population Growth-----")
    country = "JPN"
    first_year = 2014
    second_year = 2015
    value1, value2 = population_growth(country, first_year, second_year)
    print("The population growth in {} is {} in {} and {} in {}".format(country, value1, first_year, value2, second_year))
    
    print("-----Unittest-------")
    unittest.main(verbosity=2)
    print("------------")


if __name__ == "__main__":
    main()