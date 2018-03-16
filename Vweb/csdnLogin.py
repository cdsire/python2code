# -*- coding: utf-8 -*-
import selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time


driver = selenium.webdriver.Chrome()
driver.get("https://passport.csdn.net/account/login")
elem = driver.find_element_by_id("username")
elem.send_keys("")  # 这里写账号
time.sleep(3)
elem = driver.find_element_by_id("password")
elem.send_keys("")   # 这里写密码
time.sleep(4)
elem.send_keys(selenium.webdriver.common.keys.Keys.RETURN)
time.sleep(10)
print driver.page_source
driver.close()