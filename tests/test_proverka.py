import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_cards_pet(show_my_pets):
   '''Проверка карточек питомцев my_pets'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pets элементы с данными о питомцах
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Настраиваем переменную явного ожидания:
   wait = WebDriverWait(pytest.driver, 10)

   # Ожидаем, что данные всех питомцев, найденных локатором css_locator = '.table.table-hover tbody tr', видны на странице:
   for i in range(len(pets)):
      assert wait.until(EC.visibility_of(pets[i]))

   # Ищем в теле таблицы все данные фото питомцев и ожидаем увидеть их на странице:
   foto_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
   for i in range(len(foto_my_pets)):
      assert wait.until(EC.visibility_of(foto_my_pets[i]))

   # Ищем в теле таблицы все имена питомцев и ожидаем увидеть их на странице:
   name_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
   for i in range(len(name_my_pets)):
      assert wait.until(EC.visibility_of(name_my_pets[i]))

   # Ищем в теле таблицы все породы питомцев и ожидаем увидеть их на странице:
   type_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
   for i in range(len(type_my_pets)):
      assert wait.until(EC.visibility_of(type_my_pets[i]))

   # Ищем в теле таблицы все данные возраста питомцев и ожидаем увидеть их на странице:
   age_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[4]')
   for i in range(len(age_my_pets)):
      assert wait.until(EC.visibility_of(age_my_pets[i]))


