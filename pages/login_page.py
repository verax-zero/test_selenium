from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url_str = self.browser.current_url
        sub_str = "login"
        assert sub_str in url_str, "Ссылка не верная"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Форма логина не найдена"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTR), "Форма регистрации не найдена"

    def register_new_user(self, email, password):
        email_r = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTR)
        email_r.send_keys(email)
        pass_r = self.browser.find_element(*LoginPageLocators.PASS_REGISTR)
        pass_r.send_keys(password)
        pass_r_confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASS_REGISTR)
        pass_r_confirm.send_keys(password)
        btn_r = self.browser.find_element(*LoginPageLocators.BTN_REGISTR)
        btn_r.click()
        
