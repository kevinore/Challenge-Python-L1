import unittest
import app.routes.functions as function

class test_cases(unittest.TestCase):

    def test_getregions(self):
        regions = function.getRegions()
        self.assertEquals(len(regions),7)

    def test_getcoutries(self):
        regions = function.getRegions()
        countries = function.getCountries(regions)
        self.assertEquals(len(countries),248)

    def test_dateFrame(self):
        regions = function.getRegions()
        countries = function.getCountries(regions)
        df = function.createDataFrrame(countries)

        self.assertEquals(len(df.index), 248)
        self.assertEquals(len(df.columns), 4)

if __name__ == "__main__":
    unittest.main()