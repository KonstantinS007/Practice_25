import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_no_copy_names(show_my_pets):
    '''Проверка, что на странице my_pets у всех питомцев разные имена'''

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    # Сохраняем в переменную names элементы с данными о питомцах

    pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    # Поиск имен и запись в names
    names = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(2)')
    # Проверяем, что у всех питомцев разные имена:
    list_names = []
    for i in range(len(names)):
        list_names.append(names[i].text)  # Список имен
    assert len(names) == len(set(list_names))  # Равно длине списка уникальных имен
