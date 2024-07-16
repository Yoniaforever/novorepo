from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
browser = Firefox()

link = "https://google.com"

browser.get(link)

input_area = browser.find_element(By.NAME, "q")

input_area.send_keys("instituto joga junto")
input_area.send_keys(Keys.ENTER)

time.sleep(5)

result_search = browser.find_elements(By.TAG_NAME, 'h3')
print (result_search)


for result in result_search:
    if "Instituto Joga Junto" in result.text:
        result.click()
        break

field_name = browser.find_element(By.NAME, 'name').send_keys('Matheus Munhoz')
field_email = browser.find_element(By.NAME, 'email').send_keys('matheusmunhoz35@gmail.com')
field_body = browser.find_element(By.NAME, 'body').send_keys('Minha primeira automação com selenium')

field_subject = browser.find_element(By.NAME, 'assunto')
select_subject = Select(field_subject)

select_subject.select_by_visible_text('Ser facilitador')

btn_send = browser.find_element(By.XPATH, '/html/body/div/div[2]/section[8]/div[1]/form/button').submit()

