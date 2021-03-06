from selenium.webdriver.common.by import By

class LoginPageLocators():
	FORM_REGISTR = (By.CSS_SELECTOR, "#register_form")
	FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
	EMAIL_REGISTR = (By.CSS_SELECTOR, "#id_registration-email.form-control")
	PASS_REGISTR = (By.CSS_SELECTOR, "#id_registration-password1.form-control")
	CONFIRM_PASS_REGISTR = (By.CSS_SELECTOR, "#id_registration-password2.form-control")
	BTN_REGISTR = (By.NAME, "registration_submit")

class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
	PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
	NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
	NAME_PRODUCT_ADD = (By.CSS_SELECTOR, "#messages strong")
	PRICE_PRODUCT_ADD = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BTN_BASKET_PAGE = (By.CSS_SELECTOR, ".btn-group > .btn:first-child")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	TEXT_FREE_BASKET = (By.CSS_SELECTOR, "#content_inner p")
	
		
