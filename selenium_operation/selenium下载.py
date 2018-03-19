# -*- coding: utf-8 -*-
import selenium
import selenium.webdriver
import time
import os


print os.getcwd()

options = selenium.webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting.popups":0, # 下载不提示
    "download.default_directory":r"D:\new_pro"  # 下载的路劲，新版本的chrome
}
options.add_experimental_option("prefs",prefs)  # 添加实验性质的参数
driver = selenium.webdriver.Chrome()
driver.get("https://pypi.python.org/pypi/selenium")
driver.find_element_by_partial_link_text("tar.gz").click()


# # ChromeOptions的一些用法参考：https://www.cnblogs.com/wangcp-2014/p/6820542.html
# 这里设置的下载地址下载不到里面，会下载到默认的下载地址