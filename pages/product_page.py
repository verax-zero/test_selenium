from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
	price_product = ""
	name_product = ""
	name_product_add = ""
	price_product_add = ""
	def click_add_basket(self):
		basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		basket_btn.click()
		self.solve_quiz_and_get_code()

	def price_and_name(self):
		price_product =  self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
		name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
	
	def price_and_name_add(self):
		name_product_add = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADD).text
		price_product_add = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADD).text
		
	def assert_basket(self):
		assert self.name_product == self.name_product_add, "Название книги отличается"
		assert self.price_product == self.price_product_add, "Цена отличается"
