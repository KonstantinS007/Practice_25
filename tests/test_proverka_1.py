import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_in_cards(show_my_pets):
   '''Проверка того что на странице my_pets присутствуют все питомцы'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))


   pytest.driver.implicitly_wait(10)  # неявные ожидания
   pets_number = pytest.driver.find_elements(By.XPATH, '//div[@class=".col-sm-4 left"]')
   pets_number = pets_number[0].text.split('\n')[1].split(': ')[1]
   pets_count = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   assert int(pets_number) == len(pets_count)
