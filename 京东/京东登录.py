# -*- coding: utf-8 -*-
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
import requests


driver = selenium.webdriver.Chrome()
driver.get("https://passport.jd.com/new/login.aspx")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@class=\"login-tab login-tab-r\"]/a")
elem.click()    # 切换到账户登录

# 找到输入用户名/密码的地方，先清除输入格，在输入点击
user = driver.find_element_by_id("loginname")
password = driver.find_element_by_id("nloginpwd")
submit = driver.find_element_by_id("loginsubmit")
user.clear()
time.sleep(1)
user.send_keys("139*******")
password.send_keys("cd*****4")
time.sleep(1)
submit.click()
time.sleep(10)  # 等待页面加载
cookies = driver.get_cookies()  # 抓取全部的cookie
print "--"*20
print cookies
print "--"*20
driver.close()

print "开始会话"
req = requests.session()    # 会话

for cookie in cookies:
    req.cookies.set(cookie["name"],cookie["value"])
req.headers.clear() # 清空头
newpage = req.get("https://cart.jd.com/cart.action")
print "会话完成"
print newpage.text  # 页面

mytree = lxml.etree.HTML(newpage.text)
print mytree.xpath("//*[@class=\"cell p-sum\"]/strong/text()")
time.sleep(10)