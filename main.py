from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(test):
    return str(str(math.log(abs(12 * math.sin(int(test))))))


try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    wait = WebDriverWait(browser, 10)

    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    x = browser.find_element(By.ID, "input_value").text

    browser.execute_script("window.scrollBy(0, 200);")

    browser.find_element(By.NAME, 'text').send_keys(calc(int(x)))
    browser.find_element(By.ID, 'solve').click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()

