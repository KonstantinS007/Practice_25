# Practice_25


### Тесты проверок по локаторам страницы сайта PetFreinds"Мои питомцы":

    pytest test_proverka   :Проверка карточек питомцев
    pytest test_proverka_1 :Присутствуют все питомцы
    pytest test_proverka_2 :Хотя бы у половины питомцев есть фото
    pytest test_proverka_3 :У всех питомцев есть имя, возраст и порода
    pytest test_proverka_4 :У всех питомцев разные имена
    pytest test_proverka_5 :В списке нет повторяющихся питомцев

В тестах используется настройка implicitly-wait веб-драйвера. 
В тестах используются элементы класса WebDriverWait. 
```bash
pip install -r requirements.txt # зависимости 
```
```bash
python.exe -m pip install --upgrade pip # обновление
```
```bash
pytest -v -k test # запуск тестов
```
