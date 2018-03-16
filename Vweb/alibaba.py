# -*- coding: utf-8 -*-
import selenium.webdriver.common.keys
import time


driver = selenium.webdriver.Chrome()
driver.get("https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8#page/1")
time.sleep(5)
elem = driver.find_element_by_xpath("//div[@class=\"pagination\"]/ul/li[@data-index=\"next\"]/a")
elem.click()
time.sleep(20)

driver.close()