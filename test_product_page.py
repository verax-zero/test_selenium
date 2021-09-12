from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open()
	page.price_and_name()
	page.click_add_basket()
	page.price_and_name_add()
	page.assert_basket()