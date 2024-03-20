"""
@FileName：02鼠标操作.py\n
@Description：\n
@Author：bing\n
@Time：2024/3/15 15:41\n
@Department：研发部\n
@Website：www.xxx.com\n
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# url = r'D:\桌面\7月找工作\08-web自动化测试\drag.html'
url = r'D:\桌面\7月找工作\08-web自动化测试\注册A.html'

driver.get(url)

# 页面最大化
driver.maximize_window()

# 时间连对象
chains = ActionChains(driver)

# el = driver.find_element(By.XPATH, '//*[@id="div1"]')
# e2 = driver.find_element(By.XPATH, '//*[@id="div2"]')
#
# # 拖拽
# chains.drag_and_drop(el, e2)

el3 = driver.find_element(By.XPATH, '//*[@id="zc"]/fieldset/button')
# 右击：context_click（）
# 双击：double_click（）
# 拖动：drag_and_drop（）
# 悬停：move_to_element（）
chains.move_to_element(el3)

#提交
chains.perform()

time.sleep(3)

driver.quit()

