#coding:utf-8
from  selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  WebDriverWait #等待一个元素加载完成
from  selenium.webdriver.support import  expected_conditions as EC
import time

driver=webdriver.Chrome() #配置参数
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u"python 培训")

texts=driver.find_elements_by_xpath("//div/h3/a")
for text in texts:
    print text.text
time.sleep(20)
driver.close()
