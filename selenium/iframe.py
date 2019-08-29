from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mail.163.com/")

i = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(i)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("duanjing1008")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("duanjing19901008")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

driver.quit()
