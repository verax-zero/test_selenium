from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

price_product = ""
name_product = ""
name_product_add = ""
price_product_add = ""
class ProductPage(BasePage):
	
	def click_add_basket(self):
		basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		basket_btn.click()
		self.solve_quiz_and_get_code()

	def price_and_name(self):
		global price_product
		global name_product
		price_product =  self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
		name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
	
	def price_and_name_add(self):
		global name_product_add
		global price_product_add
		name_product_add = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADD).text
		price_product_add = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADD).text
		
	def assert_basket(self):
		global name_product
		global name_product_add
		global price_product
		global price_product_add
		print(name_product)
		print(name_product_add)
		assert name_product == name_product_add, "Название книги отличается"
		assert price_product == price_product_add, "Цена отличается"
	
	def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение о добавлении есть, но быть не должно"

	def test_guest_cant_see_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение о добавлении есть, но быть не должно"

	def test_message_disappeared_after_adding_product_to_basket(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение не исчесзло"
		
