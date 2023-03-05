import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


@pytest.fixture()
def show_my_pets():

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Проверяем с явным ожиданием, что мы авторизовались и оказались на главной странице /all_pets
   assert WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, "// button[contains(text(), 'Выйти')]")))
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link[href='/my_pets']")))
   # Нажимаем на ссылку "Мои питомцы"
   pytest.driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()

   # Проверяем что логин соответствует авторизации
   assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == user
