# -*- coding: utf-8 -*-
from selenium import webdriver
import time


# 设置
# deviceName:设备名称
mobile_setting = {"deviceName":"iPhone 6 Plus"}
# 选项，experimental试验，emulation模拟/仿真
options = webdriver.ChromeOptions()
# 模拟手机
options.add_experimental_option("mobileEmulation",mobile_setting)
# 配置参数
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(400,800)
driver.maximize_window()    # 全屏
driver.get("https://www.jd.com")
time.sleep(5)
driver.get("https://www.taobao.com")
time.sleep(5)
driver.back()   # 后退
time.sleep(5)
driver.forward()    # 前进
time.sleep(5)
driver.refresh()    # 刷新

driver.close()