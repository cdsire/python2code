# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 等待一个元素加载完成
from selenium.webdriver.support import expected_conditions

import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 控制操作的时间在10秒以内，如果元素出现就继续执行，如果元素不出现，最多等待10秒
driver.implicitly_wait(10)

# 最多等待15秒，必须等到这个元素出现---->节约时间，网页出现这个元素再操作
elem = WebDriverWait(driver,15).until(expected_conditions.presence_of_element_located((By.ID,"kw")))
elem.send_keys("selenium")
time.sleep(10)
driver.close()