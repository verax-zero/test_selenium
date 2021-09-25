from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()
	page.should_be_login_link()
	page_l = LoginPage(browser, browser.current_url)
	page_l.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/"
	page = BasketPage(browser, link)
	page.open()
	page.click_base_page()
	page.message_add_basket()
	page.free_basket()



