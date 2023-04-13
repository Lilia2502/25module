import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# 1 Присутствуют все питомцы
def test_all_animals_are_present(logging_in_and_go_to_my_pets, get_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    pet_stat = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    quantity = int(pet_stat[0].text.split('\n')[1].split(' ')[1])
    assert quantity == len(get_pets)


# 2 У половины питомцев есть фото
def test_pets_have_photos(logging_in_and_go_to_my_pets, get_pets, get_pets_photos):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    assert get_pets_photos >= len(get_pets) / 2


# 3 У всех питомцев есть имя, возраст и порода
def test_pets_have_photos_name_age_breed(logging_in_and_go_to_my_pets, get_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    for pet in get_pets:
        assert pet['name'] != '' and pet['age'] != '' and pet['breed'] != ''


# 4 Имена питомцев не повторяются
def test_pets_names_differ(logging_in_and_go_to_my_pets, get_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pets_name = []
    for pet in get_pets:
        if pet['name'] in pets_name:
            print("Contains")
        else:
            pets_name.append(pet)
    assert len(get_pets) == len(pets_name)


# 5 В списке отсутствуют повторяющиеся питомцы
def test_pets_differ(logging_in_and_go_to_my_pets, get_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pets = []
    for pet in get_pets:
        if pet not in pets:
            pets.append(pet)

    assert len(get_pets) == len(pets)


# 6 Проверка карточек питомцев (возраст, имя, фото)
def test_checking_by_pet_photo(logging_in_and_go_to_my_pets, get_pets, get_pets_photos):
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')
    names = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


# 7 Проверка таблицы питомцев с ожиданием
def test_checking_table_of_animals(logging_in_and_go_to_my_pets, get_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    pet_stat = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    quantity = int(pet_stat[0].text.split('\n')[1].split(' ')[1])
    assert quantity == len(get_pets)
