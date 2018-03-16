# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


'''
actionChains是一种自动化低级别交互的方式，如
     鼠标移动，鼠标按钮操作，按键和上下文菜单交互。
     这对于执行更复杂的操作（如悬停和拖放）很有用。

'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
above = driver.find_element_by_link_text(u"设置")  # 找到“设置”的所在
#当你调用perform（）时，事件按照它们的顺序被触发正在排队。
ActionChains(driver).move_to_element(above).perform()   # 鼠标停留
# ActionChains(driver).move_to_element(above).move_to_element(elem)   # 鼠标移动
ActionChains(driver).move_to_element(above).context_click() # 鼠标点击
ActionChains(driver).move_to_element(above).double_click()  # 鼠标双击
ActionChains(driver).move_to_element(above).drag_and_drop() # 拖放
time.sleep(10)
driver.close()
