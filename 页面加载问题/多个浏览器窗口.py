# -*- coding: utf-8 -*-
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.find_element_by_link_text(u"登录").click()
time.sleep(3)
driver.find_element_by_link_text(u"立即注册").click()

# 当前窗口
firstwin = driver.current_window_handle
# 所有的窗口
allwindows = driver.window_handles
# 选择注册窗口
for win in allwindows:
    if win != firstwin:
        driver.switch_to_window(win)
        print "切换成功"

        driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("hello")
        time.sleep(3)

# 关闭当前
driver.close()
time.sleep(5)
# 关闭全部
driver.quit()