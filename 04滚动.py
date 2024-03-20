import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url = r'https://www.toutiao.com'

driver.get(url)

driver.maximize_window()
time.sleep(2)
# 定义个JavaScript的脚本驱动去执行
js_str = 'window.scrollTo(0,100000)'

#执行脚本
driver.execute_script(js_str)
time.sleep(5)

driver.quit()


