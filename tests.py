import unittest

from tests_abstract import TestAbstract, TestAbstractWithAuthorizationPatient


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


class TestHomePage(TestAbstractWithAuthorizationPatient):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver.get('http://185.183.122.133/patient/')

    def test_title_in_page(self):
        self.assertIn('История', self.driver.page_source)


if __name__ == '__main__':
    unittest.main()
