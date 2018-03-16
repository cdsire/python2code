# -*- coding: utf-8 -*-
import urllib2
import lxml
import lxml.etree
import time
import selenium
import selenium.webdriver


# 找出所有页数的url
def makeurllist(url):
    driver = selenium.webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    pagesource = driver.page_source
    myetree = lxml.etree.HTML(pagesource)
    numbers = myetree.xpath("//div[@class=\"pagination\"]//a/text()")[-2]
    urllist = []
    for i in range(1,int(numbers)+1):
        urllist.append("https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8#page/"+str(i))
    driver.close()
    return urllist

def gettitlefromurl(url):
    driver = selenium.webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    pagesource = driver.page_source
    myetree = lxml.etree.HTML(pagesource)
    titlelist = myetree.xpath("//tbody[@id=\"J-list-box\"]//tr//a//text()")
    for title in titlelist:
        print title.strip()

    parturllist = myetree.xpath("//tbody[@id=\"J-list-box\"]//tr/td/span/a/@href")
    for parturl in parturllist:
        print parturl.strip()

    driver.close()

# print makeurllist("https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8#page/2")
gettitlefromurl("https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8#page/2")


