from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path
import unittest

URL = "http://google.com/"
path = "~/Documents/Myframeworkprofile"


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGoogle(self):
        profile = webdriver.FirefoxProfile(os.path.expanduser(path))
        driver = webdriver.Firefox(profile)
        driver.get(URL)
        print " today is tuesday"
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRediffmoney']
    unittest.main()
