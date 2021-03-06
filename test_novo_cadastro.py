# Generated by Selenium IDE
import pytest
import time
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test_novo_cadastro():
    def setup_method(self, method):
        self.driver = webdriver.Chrome('driver/chrome/95/chromedriver.exe')

        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_novo_cadastro(self):
        # Test name: NOVOCADASTRO
        # Step # | name | target | value | comment
        # 1 | open | /cadastro/ |  |
        self.driver.get("https://iterasys.com.br/cadastro/")
        # 2 | setWindowSize | 1575x860 |  |
        self.driver.set_window_size(1575, 860)
        # 3 | click | css=.col-md-12:nth-child(1) > h3 |  |
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-12:nth-child(1) > h3").click()
        # 4 | click | linkText=Ok! |  |
        self.driver.find_element(By.LINK_TEXT, "Ok!").click()
        # 5 | click | id=nome |  |
        self.driver.find_element(By.ID, "nome").click()
        # 6 | type | id=nome | fulano |
        self.driver.find_element(By.ID, "nome").send_keys("fulano")
        # 7 | click | css=#cadastro_form > .form-group:nth-child(2) > label |  |
        self.driver.find_element(By.CSS_SELECTOR, "#cadastro_form > .form-group:nth-child(2) > label").click()
        # 8 | type | id=telefone | (31) 9000-7009 |
        self.driver.find_element(By.ID, "telefone").send_keys("(31) 9000-7009")
        # 9 | click | id=e-captcha |  |
        self.driver.find_element(By.ID, "e-captcha").click()
        # 10 | click | id=e-captcha |  |
        self.driver.find_element(By.ID, "e-captcha").click()
        # 11 | mouseDownAt | id=e-captcha | 86.25103759765625,15.63006591796875 |
        element = self.driver.find_element(By.ID, "e-captcha")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        # 12 | mouseMoveAt | id=e-captcha | 86.25103759765625,15.63006591796875 |
        element = self.driver.find_element(By.ID, "e-captcha")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 13 | mouseUpAt | id=e-captcha | 86.25103759765625,15.63006591796875 |
        element = self.driver.find_element(By.ID, "e-captcha")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        # 14 | click | id=e-captcha |  |
        self.driver.find_element(By.ID, "e-captcha").click()
        # 15 | click | id=e-captcha |  |
        self.driver.find_element(By.ID, "e-captcha").click()
        # 16 | click | id=e-captcha |  |
        self.driver.find_element(By.ID, "e-captcha").click()
        # 17 | doubleClick | id=e-captcha |  |
        element = self.driver.find_element(By.ID, "e-captcha")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 18 | type | id=e-captcha | 44JFA3 |
        self.driver.find_element(By.ID, "e-captcha").send_keys("44JFA3")
        # 19 | click | id=btn_cadastro |  |
        self.driver.find_element(By.ID, "btn_cadastro").click()
        # 20 | click | css=.alert-robo:nth-child(1) .alert-heading |  |
        self.driver.find_element(By.CSS_SELECTOR, ".alert-robo:nth-child(1) .alert-heading").click()
        # 21 | click | id=email |  |
        self.driver.find_element(By.ID, "email").click()
        # 22 | click | id=email |  |
        self.driver.find_element(By.ID, "email").click()
        # 23 | click | id=email |  |
        self.driver.find_element(By.ID, "email").click()
        # 24 | doubleClick | id=email |  |
        element = self.driver.find_element(By.ID, "email")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 25 | click | id=email |  |
        self.driver.find_element(By.ID, "email").click()
        # 26 | type | id=email | rjr33866@cuoly.com |
        self.driver.find_element(By.ID, "email").send_keys("rjr33866@cuoly.com")
        # 27 | click | id=senha |  |
        self.driver.find_element(By.ID, "senha").click()
        # 28 | type | id=senha | tESTE@2570 |
        self.driver.find_element(By.ID, "senha").send_keys("tESTE@2570")
        # 29 | click | id=e-captcha |  |
        self.driver.find_element(By.ID, "e-captcha").click()
        # 30 | type | id=e-captcha | I5GURZ |
        self.driver.find_element(By.ID, "e-captcha").send_keys("I5GURZ")
        # 31 | click | id=btn_cadastro |  |
        self.driver.find_element(By.ID, "btn_cadastro").click()
        # 32 | click | css=.alert-heading:nth-child(2) |  |
        self.driver.find_element(By.CSS_SELECTOR, ".alert-heading:nth-child(2)").click()
        # 33 | assertChecked | css=.alert-heading:nth-child(2) |  |
        assert self.driver.find_element(By.CSS_SELECTOR, ".alert-heading:nth-child(2)").is_selected() is True
        # 34 | click | linkText=Fa??a o Login |  |
        self.driver.find_element(By.LINK_TEXT, "Fa??a o Login").click()
        # 35 | mouseDownAt | id=email | 16.25103759765625,11.078765869140625 |
        element = self.driver.find_element(By.ID, "email")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        # 36 | mouseMoveAt | id=email | 16.25103759765625,11.078765869140625 |
        element = self.driver.find_element(By.ID, "email")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 37 | mouseUpAt | id=email | 16.25103759765625,11.078765869140625 |
        element = self.driver.find_element(By.ID, "email")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        # 38 | click | id=email |  |
        self.driver.find_element(By.ID, "email").click()
        # 39 | type | id=email | rjr33866@cuoly.com |
        self.driver.find_element(By.ID, "email").send_keys("rjr33866@cuoly.com")
        # 40 | click | id=senha |  |
        self.driver.find_element(By.ID, "senha").click()
        # 41 | type | id=senha | tESTE@2570 |
        self.driver.find_element(By.ID, "senha").send_keys("tESTE@2570")
        # 42 | click | id=btn_login |  |
        self.driver.find_element(By.ID, "btn_login").click()
        # 43 | click | css=.alert:nth-child(3) > h4 |  |
        self.driver.find_element(By.CSS_SELECTOR, ".alert:nth-child(3) > h4").click()
        # 44 | click | css=.login .col-md-12 |  |
        self.driver.find_element(By.CSS_SELECTOR, ".login .col-md-12").click()

