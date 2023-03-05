import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_photo_pets(show_my_pets):
    '''Проверяем что на странице my_pets хотя бы у половины питомцев есть фото'''

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    ages = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(4)')
    pets_count = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    images = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > th > img')

    number_image = 0
    half_num = float((len(pets_count) - 1)/2)

    for i in range(len(ages)):
       if images[i].get_attribute('src') != '':
          number_image += 1
       else:
          number_image = number_image
    assert number_image >= half_num