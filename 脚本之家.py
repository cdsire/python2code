# -*- coding: utf-8 -*-
import urllib2
import lxml
import lxml.etree
import re


# 找出所有页数的url
def makeurllist(url):
    headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers)
    data = urllib2.urlopen(request).read()
    myetree = lxml.etree.HTML(data)
    lastlist = myetree.xpath("//div[@class=\"dxypage clearfix\"]//text()")[0]
    print lastlist  # 页次：1/212 每页40 文章数8448
    re_str = u"页次：1/(\d+) 每页"
    regex = re.compile(re_str,re.IGNORECASE)
    sumpage = regex.findall(lastlist)[0]
    print sumpage    # 总页数

    urllist = []
    for i in range(1,int(sumpage) + 1):
        urllist.append("http://www.jb51.net/list/list_97_"+str(i)+".htm")
    return urllist  # 脚本之家所有的链接列表

def gettitlefromurl(url):
    lastlist = []   # 用来存储标题和对应的url
    headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers)
    data = urllib2.urlopen(request).read()
    myetree = lxml.etree.HTML(data)

    # http://www.jb51.net/article/135899.htm

    dtlist = myetree.xpath("//div[@class=\"artlist clearfix\"]//dt")
    for dt in dtlist:
        print dt.xpath(".//a/text()")[0],"http://www.jb51.net"+dt.xpath(".//a/@href")[0]
    #
    #
    # parturllist =myetree.xpath("//div[@class=\"artlist clearfix\"]//dt/a/@href")
    # for urllist in parturllist:
    #     titleurllist = "http://www.jb51.net" + urllist
    #
    # titlelist = myetree.xpath("//div[@class=\"artlist clearfix\"]//dt/a/text()")
    # for title in titlelist:
    #     print title,titleurllist


# print makeurllist("http://www.jb51.net/list/list_97_1.htm")
gettitlefromurl("http://www.jb51.net/list/list_97_1.htm")