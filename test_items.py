import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_add_to_basket_button(browser, link):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), "There is no \"Add to basket\" button"