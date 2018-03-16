# encoding:utf-8
import urllib2
import cookielib


filepath = "cookie.txt"
cookie = cookielib.LWPCookieJar()   # 设定路径
cookie.load(filepath,ignore_discard=False,ignore_expires=False)

header = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(header)
response = opener.open("http://www.renren.com/")
print response.read()