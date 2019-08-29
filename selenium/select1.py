from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

driver.find_element_by_link_text("设置").click()
sleep(5)
driver.find_element_by_link_text("搜索设置").click()
sleep(7)

sel = driver.find_element_by_name("NR")
Select(sel).select_by_value('50')
sleep(10)

driver.quit()
