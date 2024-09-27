import unittest
from abc import ABCMeta

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# TODO: Need path TO YOU geckodriver, for example it's my path.
PATH_TO_FIREFOX_WEBDRIVER = '/home/ubunu/intership_step_3_selenium/geckodriver'
HOST = 'http://185.183.122.133'


class TestAbstract(unittest.TestCase, metaclass=ABCMeta):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(executable_path=PATH_TO_FIREFOX_WEBDRIVER)


class TestAbstractWithLogin(unittest.TestCase, metaclass=ABCMeta):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(executable_path=PATH_TO_FIREFOX_WEBDRIVER)
        cls.driver.get(f"{HOST}")
        login = cls.driver.find_element_by_id('id_username')
        login.clear()
        login.send_keys("patient_for_tests")
        pswd = cls.driver.find_element_by_id('id_password')
        pswd.send_keys("UzEMaxrc7D")
        pswd.submit()


class TestAbstractWithAuthorizationPatient(TestAbstractWithLogin, metaclass=ABCMeta):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        WebDriverWait(cls.driver, 10).until(EC.url_to_be(f"{HOST}/patient/"))
