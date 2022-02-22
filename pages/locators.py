from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
class LoginPageLocators():
    LOGIN_USER = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

