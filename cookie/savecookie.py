# encoding:utf-8
import urllib2
import cookielib


filepath = "cookie.txt"
cookie = cookielib.LWPCookieJar(filepath)   # 设定路径
header = urllib2.HTTPCookieProcessor(cookie)    # 设置cookie，与网站有关
opener = urllib2.build_opener(header)
response = opener.open("http://www.baidu.com")

cookie.save(ignore_expires=True,ignore_discard=True)    # 忽略