from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import ctime
from selenium.common.exceptions import NoSuchElementException

driver_c = webdriver.Chrome()
driver_c.get("https://www.baidu.com")

'''
element = WebDriverWait(driver_c, 5, 0.5).until(
    expected_conditions.presence_of_all_elements_located((By.ID, "kw"))
)
element.send_keys("selenuim")
'''

driver_c.implicitly_wait(10)

try:
    print(ctime())
    driver_c.find_element_by_id("kw").send_keys("selenuim")
except NoSuchElementException:
    print(NoSuchElementException)
finally:
    print(ctime())
    driver_c.quit()
