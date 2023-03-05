import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_name_types_age(show_my_pets):
   '''Поверяем, что на странице my_pets у всех питомцев есть имя, порода и возраст'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
   # Поиск имени запись в names
   names = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(2)')
   # Поиск вида запись в types
   types = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(3)')
   # Поиск возраста запись в возраста
   ages = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(4)')
   # Проверки списков на наличие данных
   for i in range(len(ages)):
      assert ages[i].text != ''
      assert names[i].text != ''
      assert types[i].text != ''
