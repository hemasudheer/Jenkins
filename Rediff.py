from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

URL = "http://money.rediff.com/"
locators = {"searchbox": "//*[@id='srchword']",
            "quotebutton": "//*[contains(@class,'btn_srch')]",
            "pageready": "//span[contains(@class, 'moneywizlogo')]",
            "req_company": "//*[@id='for_BSE']/h1"
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
        driver.implicitly_wait(10)
        webpagename = driver.find_element_by_xpath(locators['pageready'])
        print "webpage is " + webpagename.text
        #assert webpagename.text == "Rediff Moneywiz"
        element = driver.find_element_by_xpath(locators['searchbox'])
        element.send_keys(company_name)
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        company = driver.find_element_by_xpath(locators['req_company'])
        print "Current company is " + company.text
        assert company_name in company.text
        print "edited from eclipse"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRediffmoney']
    unittest.main()
