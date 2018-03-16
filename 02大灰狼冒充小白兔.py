# coding:utf-8
# urlib.request == urllib2
import urllib2

def download(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
    }
    request = urllib2.Request(url,heades=headers)  # 发起请求
    data = urllib2.urlopen(request).read()  # 打开请求，抓取数据
    return data

def download2(url):
    return urllib2.urlopen(url).read()


url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=java&p=1&isadv=0"
print download2(url)
