import time

from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.baidu.com"

driver.get(url)
driver.maximize_window()

driver.get_screenshot_as_file('baidu1.png')

# 设置cookie
driver.add_cookie({"name": "BAIDUID", "value": "376AC7FA60C24255799DEACA7F3ABF1F:FG=1"})
driver.add_cookie({"name": "BDUSS",
                   "value": "pXWC1zZTZtVjktYkd3Vm82bGp6cDVFNy1qUi1BYzVOLTFmS3ZDTWItVHN0U1JtRUFBQUFBJCQAAAAAAAAAAAEAAABcnlhRsru74cjau6-1xLqusfkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOwo~WXsKP1lOU"})


time.sleep(2)
driver.refresh()
driver.get_screenshot_as_file('baidu2.png')
time.sleep(10)
driver.quit()




