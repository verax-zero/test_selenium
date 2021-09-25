from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
from .locators import ProductPageLocators

class BasketPage(BasePage):

	def free_basket(self):
		text_basket = "Ваша корзина пуста Продолжить покупки"
		free_basket_text =  self.browser.find_element(*BasketPageLocators.TEXT_FREE_BASKET).text
		assert text_basket == free_basket_text, "Корзина не пуста"

	def message_add_basket(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Корзина не пуста, присутствует сообщение о добавлении товара"