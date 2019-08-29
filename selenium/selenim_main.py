from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver_c = webdriver.Chrome()
driver_c.get("https://www.baidu.com")


driver_c.find_element_by_id("kw").send_keys("selenuim")

driver_c.find_element_by_id("su").click()  # 点击
sleep(5)
texes = driver_c.find_elements_by_xpath('/div[1]/h3/a')

for t in texes:
    print(t.text)
driver_c.quit()

# driver_c.find_element_by_id("su").submit()  # 提交

'''
size = driver_c.find_element_by_id("kw").size
print(size)

text = driver_c.find_element_by_id("cp").text
print(text)

atrribute = driver_c.find_element_by_id("kw").get_attribute('name')
print(atrribute)

result = driver_c.find_element_by_id("kw").is_displayed()
print(result)


above = driver_c.find_element_by_link_text("设置")
ActionChains(driver_c).move_to_element(above).perform()


driver_c.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

driver_c.find_element_by_id("kw").clear()

driver_c.find_element_by_id("kw").send_keys(Keys.SPACE)
driver_c.find_element_by_id("kw").send_keys("哈哈")

driver_c.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
driver_c.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
driver_c.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
driver_c.find_element_by_id("kw").send_keys(Keys.ENTER)
'''




