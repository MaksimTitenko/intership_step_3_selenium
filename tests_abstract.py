import unittest

from selenium import webdriver


class TestAbstract(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        '''Need path TO YOU geckodriver, it's my path.'''
        cls.driver = webdriver.Firefox(executable_path='/home/maksim/Internship/intership_step_3_selenium/geckodriver')

class TestAbstractWithLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        '''Need path TO YOU geckodriver, it's my path.'''
        profile = webdriver.FirefoxProfile()
        cls.driver = webdriver.Firefox(executable_path='/home/maksim/Internship/intership_step_3_selenium/geckodriver')
        cls.driver.get("http://185.183.122.133/")
        login = cls.driver.find_element_by_id('id_username')
        login.clear()
        login.send_keys("patient_for_tests")
        pswd = cls.driver.find_element_by_id('id_password')
        pswd.send_keys("UzEMaxrc7D")
        pswd.submit()


