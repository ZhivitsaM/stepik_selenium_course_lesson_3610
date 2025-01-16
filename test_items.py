from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition


def test_basket_button_is_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Проверка наличии кнопки добавления товара в корзину
    button = WebDriverWait(browser, 10).until(
        condition.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )
    assert button, "There is no button to add item to basket!"

    time.sleep(30)
