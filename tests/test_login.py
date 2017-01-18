import unittest
from selenium import webdriver
from tests.poms.poms import LoginPOM

class LoginTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.driver.get("http://pluszaki.pl:8000/account/login/")

	def test_login_and_logout(self):
		login_page = LoginPOM(self.driver)

		self.assertFalse(login_page.is_logged_in())

		login_page.fill_login_fields()
		login_page.execute_login()

		self.assertTrue(login_page.is_logged_in())

		login_page.execute_logout()

		self.assertFalse(login_page.is_logged_in())

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
