from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверкa на корректный url адрес
        assert login in self.browser.currernt_url=self.url,"Login is not in url"
        #:assert True

    def should_be_login_form(self):
        # проверкa, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Forma login is not presented"
        #assert True

    def should_be_register_form(self):
        # проверкa, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Forma registration is not presented"
        #assert True
