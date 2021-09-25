from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.login
class TestUserAddToBasketFromProductPage():

	
	@pytest.fixture(scope="function", autouse=True)
	def test_register_n_user(self, browser):
		email = str(time.time()) + "@mail.com"
		link = "http://selenium1py.pythonanywhere.com/ru/"
		page = LoginPage(browser, link)
		page.open()
		page.go_to_login_page()
		page.register_new_user(email, "pl,okmijnuy")
		page.should_be_authorized_user()
	
	def test_user_can_add_product_to_basket(self, browser):
		link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
		page = ProductPage(browser, link)
		page.open()
		page.price_and_name()
		page.click_add_basket()
		page.price_and_name_add()
		page.assert_basket()

	def test_user_can_add_product_to_basket_messages(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
		page = ProductPage(browser, link)
		page.open()
		page.test_guest_cant_see_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
		pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
		page = ProductPage(browser, link)
		page.open()
		page.price_and_name()
		page.click_add_basket()
		page.price_and_name_add()
		page.assert_basket()

def test_guest_can_add_product_to_basket_messages(browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
		page = ProductPage(browser, link)
		page.open()
		page.test_guest_cant_see_success_message()


@pytest.mark.xfail
def test_guest_can_add_product_to_basket_messages_disappeared(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
	page = ProductPage(browser, link)
	page.open()
	page.click_add_basket()
	page.test_message_disappeared_after_adding_product_to_basket()
	
@pytest.mark.xfail
def test_guest_can_add_product_to_basket_messages_after_add(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
	page = ProductPage(browser, link)
	page.open()
	page.click_add_basket()
	page.test_guest_cant_see_success_message_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
	page = BasketPage(browser, link)
	page.open()
	page.click_base_page()
	page.message_add_basket()
	page.free_basket()
