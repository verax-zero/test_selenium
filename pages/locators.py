from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	FORM_REGISTR = (By.CSS_SELECTOR, "#register_form")
	FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
