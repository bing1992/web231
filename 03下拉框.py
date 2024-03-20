import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url = r'D:\桌面\7月找工作\08-web自动化测试\注册A.html'

driver.get(url)

driver.maximize_window()

select1 = Select(driver.find_element(By.XPATH, '//*[@id="selectA"]'))
time.sleep(2)

select1.select_by_index(2)
time.sleep(2)
select1.select_by_value("bj")
time.sleep(2)
select1.select_by_visible_text("A重庆")
time.sleep(2)

driver.quit()


