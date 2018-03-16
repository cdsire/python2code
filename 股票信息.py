# -*- coding: utf-8 -*-
import urllib2
import lxml
import lxml.etree


def download(url):
    headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers)
    data = urllib2.urlopen(request).read()
    myetree = lxml.etree.HTML(data)
    datalist = myetree.xpath("//div[@class=\"text-column-list mt10\"]//h3//a//text()")
    print datalist
    for linedata in datalist:
        print linedata





download("http://www.neihanpa.com/article/")








'''
import urllib2
import lxml
import lxml.etree


def download(url):
    headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers)
    data = urllib2.urlopen(request).read()
    myetree = lxml.etree.HTML(data)

'''