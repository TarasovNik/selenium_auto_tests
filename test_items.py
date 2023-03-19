import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_add_to_basket_button(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")