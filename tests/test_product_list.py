import unittest
from selenium import webdriver
from tests.poms.poms import ProductsListPOM

class LoginTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.driver.get("http://pluszaki.pl:8000/")

	def test_product_list(self):
		products_page = ProductsListPOM(self.driver)

		self.assertTrue(products_page.check_if_products_page())

		all_products_count = products_page.get_number_of_products()
		products_page.change_category()
		category_products_count = products_page.get_number_of_products()

		self.assertTrue(all_products_count > category_products_count)

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
