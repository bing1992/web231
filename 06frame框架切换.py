import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url = r'https://mail.qq.com'
driver.get(url)
driver.maximize_window()


el1 = driver.find_element(By.XPATH, '//*[@id="login_pictures"]/div[2]')
print(el1.text)

# 子页面切换
frame1 = driver.find_element(By.XPATH, '//*[@id="QQMailSdkTool_login_loginBox_qq"]/iframe')
driver.switch_to.frame(frame1)
time.sleep(3)
frame2 = driver.find_element(By.XPATH, '//*[@id="ptlogin_iframe"]')
driver.switch_to.frame(frame2)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="switcher_plogin"]').click()
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys("1520325759")
driver.find_element(By.XPATH, '//*[@id="p"]').send_keys("xiaomi1992")
time.sleep(2)
# driver.switch_to.frame(frame1)
driver.find_element(By.XPATH, '//*[@id="loginform"]/div[4]/a').click()
time.sleep(2)


# //*[@id="QQMailSdkTool_login_loginBox_qq"]/iframe

# //*[@id="iframe_wx"]





driver.quit()

