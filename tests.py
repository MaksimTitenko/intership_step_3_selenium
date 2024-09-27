from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from tests_abstract import *


class TestLoginPage(TestAbstract):
    '''
    login for patient: patient_for_tests
    password: UzEMaxrc7D
    '''

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver.get(f"{HOST}")  # login page

    def test_title_in_page(self):
        self.driver.get(f"{HOST}")
        self.assertIn("Софит-Здоровье", self.driver.title)

    def test_login_in_page(self):
        self.driver.get(f"{HOST}")
        login = self.driver.find_element_by_id('id_username')
        login.send_keys("patient_for_tests")
        login.submit()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "errorlist"), "Это поле обязательно."))
        except TimeoutException:
            self.assert_(False, 'Element "errorlist not in page"')

    def test_password_in_page(self):
        self.driver.get(f"{HOST}")
        pswd = self.driver.find_element_by_id('id_password')
        pswd.send_keys("UzEMaxrc7D")
        pswd.submit()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "errorlist"), "Это поле обязательно."))
        except TimeoutException:
            self.assert_(False, 'Element "errorlist" not in page')

    def test_input_incorrect_login_password_in_page(self):
        self.driver.get(f"{HOST}")
        login = self.driver.find_element_by_id('id_username')
        login.send_keys("patient_for_tut")
        pswd = self.driver.find_element_by_id('id_password')
        pswd.send_keys("QWERTY")
        pswd.submit()
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='alert alert-dismissible fade show alert-warning']")))
        except TimeoutException:
            self.assert_(False, 'Element "alert alert-dismissible fade show alert-warning" not in page')

    def test_entry_in_page(self):
        self.driver.get(f"{HOST}")
        login = self.driver.find_element_by_id('id_username')
        login.send_keys("patient_for_tests")
        pswd = self.driver.find_element_by_id('id_password')
        pswd.send_keys('UzEMaxrc7D')
        pswd.submit()
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be(f"{HOST}/patient/"))
        except TimeoutException:
            self.assert_(False, 'Try again')


class TestHomePage(TestAbstractWithAuthorizationPatient):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver.get(f"{HOST}/patient/")

    def test_title_in_page(self):
        self.driver.get(f"{HOST}/patient/")
        self.driver.find_element_by_link_text('История').click()
        self.assertIn('История событий вашего личного кабинета', self.driver.page_source)

    def test_doctors_appointment_in_page(self):
        self.driver.get(f"{HOST}/patient/")
        self.driver.find_element_by_link_text('Записаться').click()
        self.assertIn('Выберите специализацию доктора', self.driver.page_source)

    def test_counseling_in_page(self):
        self.driver.get(f"{HOST}/patient/")
        self.driver.find_element_by_link_text('Консультации').click()
        self.assertIn('Все мои консультации', self.driver.page_source)
        self.assertIn('Запланированные визиты', self.driver.page_source)
        self.assertIn('Прошедшие визиты', self.driver.page_source)

    def test_my_file_in_page(self):
        self.driver.get(f"{HOST}/patient/")
        self.driver.find_element_by_link_text('Мои файлы').click()
        self.assertIn('Файлы пациента', self.driver.page_source)

    def test_chat_callcenter_in_page(self):
        self.driver.get(f"{HOST}/patient/")
        self.driver.find_element_by_link_text('Чат с колл- центром').click()
        self.assertIn('Чат с колл-центром', self.driver.page_source)


if __name__ == '__main__':
    unittest.main()
