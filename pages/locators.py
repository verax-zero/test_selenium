from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	FORM_REGISTR = (By.CSS_SELECTOR, "#register_form")
	FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
	PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
	NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
	NAME_PRODUCT_ADD = (By.CSS_SELECTOR, "#messages strong")
	PRICE_PRODUCT_ADD = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")

	
		
