import unittest
from selenium import webdriver
from tests.poms.poms import ProductsListPOM, ItemPOM, CartPOM, OrderPOM

class LoginTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.driver.get("http://pluszaki.pl:8000/")

	def test_workflow(self):
		products_page = ProductsListPOM(self.driver)

		self.assertTrue(products_page.check_if_products_page())
		first_item_page = products_page.go_to_first_product_by_name_link()

		self.assertTrue(first_item_page.check_if_item_page())
		self.assertTrue(first_item_page.is_cart_empty())

		cart_page = first_item_page.add_item_to_cart()
		self.assertTrue(cart_page.check_if_cart_page())

		self.assertFalse(cart_page.is_cart_empty())

		one_item_price = cart_page.get_total_price()

		self.assertEqual(cart_page.get_item_types_count(), 1)

		products_page = cart_page.return_to_products()
		last_item_page = products_page.go_to_last_product_by_image_link()

		self.assertTrue(last_item_page.check_if_item_page())

		cart_page = last_item_page.add_item_to_cart()
		
		self.assertEqual(cart_page.get_item_types_count(), 2)

		two_items_price = cart_page.get_total_price()
		self.assertTrue(two_items_price > one_item_price)
		
		cart_page.remove_first_item_from_cart()
		self.assertEqual(cart_page.get_item_types_count(), 1)

		order_page = cart_page.create_new_order()
		self.assertTrue(order_page.check_if_order_page())
		self.assertEqual(order_page.get_number_of_order_items_types(), 1)
		

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
