from selenium import webdriver

brower = webdriver.Chrome()

first_url = 'http://www.baidu.com'
print("当前地址是 %s" %(first_url) )
brower.get(first_url)

second_url = 'http://news.baidu.com'
print("当前地址是 %s" %(second_url))
brower.get(second_url)

brower.back()   # 退回到第一个

brower.forward()  # 前进到第二个

brower.quit()