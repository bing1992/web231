import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url = r'D:\桌面\7月找工作\08-web自动化测试\注册A.html'

driver.get(url)

driver.maximize_window()
# 点出弹框
driver.find_element(By.XPATH, '//*[@id="alerta"]').click()
time.sleep(2)
#切换到弹窗
alert = driver.switch_to.alert
print(alert.text)
# 确认方式取消警告框
# alert.dismiss()
# # 通过取消方式
alert.accept()

time.sleep(2)
driver.quit()


