from selenium import webdriver

from tests_abstract import TestAbstract, TestAbstractWithLogin


class TestLoginPage(TestAbstract):
    '''
    login for patient: patient_for_tests
    password: UzEMaxrc7D
    '''

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver.get('http://185.183.122.133/')  # login page

    def test_title_in_page(self):
        self.assertIn("Софит-Здоровье", self.driver.title)

class TestHomePage(TestAbstractWithLogin):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.driver.get('http://185.183.122.133/patient')  # login page

    def test_title_in_page(self):
        self.assertIn("Софит-Здоровье", self.driver.title)