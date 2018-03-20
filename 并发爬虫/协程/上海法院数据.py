# -*- coding: utf-8 -*-
import gevent
import gevent.monkey
import selenium
import selenium.webdriver
import time

from bs4 import BeautifulSoup


gevent.monkey.patch_all()   # 协程间自动切换
def download(url,start,end,file):
    driver = selenium.webdriver.PhantomJS("D:\new_pro\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    driver.get(url)
    gevent.sleep(10)

    for i in range(start,end):
        # 通过页码的js来循环页面
        js = "javascript:goPage('"+str(i)+"')"
        driver.execute_script(js)
        print "js is runing",i
        gevent.sleep(10)

        # 提取页面数据
        soup = BeautifulSoup(driver.page_source,"lxml") # 解析数据
        table = soup.find("table",attrs={"id":"report"})
        trs = table.find("tr").find_next_siblings()
        for tr in trs:
            tds = tr.find_all("td")
            # 用来拼合数据
            linestr = ""
            for td in tds:
                linestr += td.text
                linestr += " # "
            linestr += "\r\n"
            print linestr
            file.write(linestr.encode("utf-8",errors="ignore"))
        driver.quit()

url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search.jsp"
file = open("save.txt","wb")
gevent.joinall([
    gevent.spawn(download,url,0,2,file),
    gevent.spawn(download,url,2,4,file),
    gevent.spawn(download,url,4,6,file),
    gevent.spawn(download,url,6,8,file),
    gevent.spawn(download,url,8,10,file),
])
file.close()

