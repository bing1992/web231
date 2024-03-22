import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.jd.com/"

driver.get(url)
driver.maximize_window()
# 获取当前浏览器所有页面信息：返回列表
print(driver.window_handles)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="navitems-group1"]/li[8]/a').click()

print(driver.current_window_handle)
print(driver.window_handles)
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.quit()
