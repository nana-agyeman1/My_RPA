import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(executable_path='C:\Python38\geckodriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application homepage
        self.driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("jewelry")
        self.search_field.submit()

        # get all the anchor elements which have the product names
        # displayed currently on result page by using 
        # find_elements_by_xpath method 
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))

    
    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("shirts")
        self.search_field.submit()

        # get all the anchor elements which have the product names
        # displayed currently on result page by using 
        # find_elements_by_xpath method 
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(2, len(products))

    def tearDown(self):
        # close the browser window 
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)