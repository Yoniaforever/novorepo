from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

browser = Firefox()

link = "https://google.com"

browser.get(link)

input_area = browser.find_element(By.NAME, "q")

input_area.send_keys("instituto joga junto")
input_area.send_keys(Keys.ENTER)

result_search = browser.find_elements(By.NAME, "h3")
print (result_search)

check = False
for result in result_search:
    if "Instituto Joga Junto" in result.text:
        result.click()
        check = True

