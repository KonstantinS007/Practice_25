import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_no_duplicate_pets(show_my_pets):
    '''Проверка того что на странице my_pets нет повторяющихся питомцев'''

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pytest.driver.implicitly_wait(10)  # Неявные ожидания (сек)
    # Поиск данных питомцев и запись в all_pets
    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    # Проверяем, что у всех питомцев разные данные хоть чем-то отличаются:
    pets = []
    for pet in all_pets:
        pets.append(pet.text)  # Список данных
    assert len(set(pets)) == len(pets)  # Равно длине списка уникальных данных
