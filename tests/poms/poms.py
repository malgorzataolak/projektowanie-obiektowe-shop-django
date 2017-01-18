class PagePOM(object):
	def __init__(self, driver):
		self.driver = driver

	def is_cart_empty(self):
		return True if "pusty" in self.driver.find_element_by_class_name("cart").text else False

	def is_logged_in(self):
		return True if "Witaj" in self.driver.find_element_by_class_name("login").text else False
		

class ProductsListPOM(PagePOM):

	def check_if_products_page(self):
		return True if self.driver.find_element_by_tag_name("h1").text == "Produkty" else False

	def get_number_of_products(self):
		products = self.driver.find_elements_by_class_name("item")
		return len(products)

	def change_category(self, category="product_list_selectbycategory"):
		self.driver.find_element_by_id(category).click()

	def go_to_first_product_by_name_link(self):
		self.driver.find_elements_by_id("product_list_productnameproductdetail")[0].click()
		return ItemPOM(self.driver)

	def go_to_last_product_by_image_link(self):
		self.driver.find_elements_by_id("product_list_imgproductdetail")[-1].click()
		return ItemPOM(self.driver)


class ItemPOM(PagePOM):
	
	def check_if_item_page(self):
		return True if self.driver.find_elements_by_class_name("product-detail") else False

	def add_item_to_cart(self):
		self.driver.find_element_by_id("product_detail_addtocart").click()
		return CartPOM(self.driver)


class CartPOM(PagePOM):

	def check_if_cart_page(self):
		return True if "zakupy" in self.driver.find_element_by_id("cart_detail_continueshopping").text else False

	def get_total_price(self):
		mixed_text = self.driver.find_element_by_id("main_cartdetail").text
		cleaned_text = mixed_text.split(",")[1].strip()[:-3]
		price = float(cleaned_text)
		return price

	def get_item_types_count(self):
		item_types = self.driver.find_elements_by_id("cart_detail_name")
		return len(item_types)

	def remove_first_item_from_cart(self):
		self.driver.find_element_by_id("cart_detail_removeproduct").click()

	def create_new_order(self):
		self.driver.find_element_by_id("cart_detail_createorder").click()
		return OrderPOM(self.driver)

	def return_to_products(self):
		self.driver.find_element_by_id("cart_detail_continueshopping").click()
		return ProductsListPOM(self.driver)


class OrderPOM(PagePOM):

	def check_if_order_page(self):
		return True if self.driver.find_element_by_tag_name("h1").text == "Kasa" else False
		

	def get_number_of_order_items_types(self):
		order_items_types = self.driver.find_elements_by_tag_name("li")
		return len(order_items_types)


class LoginPOM(PagePOM):

	def fill_login_fields(self, username="gosia", password="gosia1"):
		self.driver.find_element_by_id("id_username").send_keys(username)
		self.driver.find_element_by_id("id_password").send_keys(password)

	def execute_login(self):
		self.driver.find_element_by_id("account_registration_login").click()

	def execute_logout(self):
		self.driver.find_element_by_id("main_logout").click()
		
