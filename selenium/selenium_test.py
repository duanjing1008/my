from selenium import webdriver     # 导入webdriver模块

browser_c = webdriver.Chrome()     # 打开谷歌浏览器
browser_c.get("https://www.baidu.com")

'''
print("设置浏览器宽480、高800的显示")
browser_c.set_window_size(480, 800)  #设置窗口高宽
'''

# input = browser_c.find_element_by_id("kw")  # 通过ID定位输入框
input = browser_c.find_element_by_xpath('//*[@id="kw"]')
input.send_keys('python')   # 在输入框输入Python

print(browser_c.current_url)  # 打印当前网页地址
print(browser_c.page_source)  # 打印网页源码

browser_c.close()    #关闭浏览器
