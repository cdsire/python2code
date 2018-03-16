# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 等待一个元素加载完成
from selenium.webdriver.support import expected_conditions

import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 控制操作的时间在10秒以内，如果u元素出现就继续执行，如果元素不出现，最多等待10秒
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u"鲁迅")

# 如果数量显示了就打印内容
if driver.find_element_by_class_name("nums").is_displayed():
    print driver.find_element_by_class_name("nums").text

driver.close()
