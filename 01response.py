# coding:utf-8
# urlib.request == urllib2
import urllib2


def download(url):
    response = urllib2.urlopen(url,timeout=10)   #超时
    print(type(response))
    # print(response.info())  # 包含了网站请求的详细信息
    print response.read(100)    #read()读取全部，read(100)

try:
    print(download("http://www.google.com"))    # 抓住错误类型当作变量
except urllib2.URLError as e:
    print ("web error : ",e)