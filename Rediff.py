'''
Created on Sep 19, 2014

@author: hemasudheer
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

URL = "http://money.rediff.com/"
locators = {"searchbox": "//*[@id='srchword']",
            "quotebutton": "//*[contains(@class,'btn_srch')]"
            }
company_name = "JK Cement Ltd."


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRediffmoney(self):
        driver = webdriver.Firefox()
        driver.get(URL + "gainers/bse")
        print "this is for git verification"
        #assert "Rediff Moneywiz" in driver.title()
        element = driver.find_element_by_xpath("//*[@id='srchword']")
        element.send_keys(company_name)
        print "this id for vommiting from local repo"
        element.send_keys(Keys.RETURN)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRediffmoney']
    unittest.main()
