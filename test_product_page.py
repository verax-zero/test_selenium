from .pages.product_page import ProductPage
import pytest



#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#		"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
	page = ProductPage(browser, link)
	page.open()
	#page.price_and_name()
	#page.test_guest_cant_see_success_message()
	page.click_add_basket()
	#page.price_and_name_add()
	#page.assert_basket()
	#page.test_message_disappeared_after_adding_product_to_basket()
	page.test_guest_cant_see_success_message_after_adding_product_to_basket()
