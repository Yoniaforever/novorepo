from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time

browser = Firefox()

link = "https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html"

browser.get(link)

btn_add_element = browser.find_element(By.ID, "addElement")


for i in range(10):
    btn_add_element.click()

checkbox = browser.find_elements(By.TAG_NAME, "input")

for checkbox in checkbox:
    checkbox.click()

time.sleep(5)

browser.quit