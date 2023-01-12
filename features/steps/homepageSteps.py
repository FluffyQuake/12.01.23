from behave import when
from selenium.webdriver.common.by import By
import time

URL = "https://www.ametikool.ee"

@when("I open URL")
def openURL(context):
    context.driver.get("URL")

@then('I check homepage is opened')
def checkURL(context):
    driver = context.driver
    assert driver.current_url == URL

    menuAvaleht = driver.find_element(By.CSS_SELECTOR, ".header-nav_main > li:nth-child(1) > a:nth-child(1)")
    assert menuAvaleht.is_displayed()
    assert menuAvaleht.text == "AVALEHT"

@when("I search for {keyword}")
def search(context, keyword):
    driver = context.driver
    searchfield = driver.find_element(By.CSS_SELECTOR, ".header-search > input:nth-child(1)")
    searchfield.send_keys(keyword)
    driver.find_element(By.CSS_SELECTOR, ".header-search > input:nth-child(1)")
    searchButton.click()
    time.sleep(2)

@then("Testimine is found")
def keywordIsFound(context, keyword):
    driver = context.driver
    keywordFound = driver.find_element(By.CSS_SELECTION, "")
    assert keyword in keywordFound.text