# -*- coding: utf-8 -*-
import selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time


driver = selenium.webdriver.Chrome()
driver.get("http://www.baidu.com")
elem = driver.find_element_by_id("kw")
elem.send_keys(u"鲁迅")
time.sleep(3)
# 将输入的内容点击回车
elem.send_keys(selenium.webdriver.common.keys.Keys.RETURN)

time.sleep(20)
driver.close()