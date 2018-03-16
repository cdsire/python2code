# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("hello")
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)  # 后退

time.sleep(5)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"c")
time.sleep(10)
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(4)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"v")
time.sleep(5)
driver.close()