# encoding:utf-8
import urllib2
import cookielib

# 创建一个对象存储cookie
cookie = cookielib.CookieJar()
# 自动提取cookie
header = urllib2.HTTPCookieProcessor(cookie)
# 处理cookie
opener = urllib2.build_opener(header)
response = opener.open("http://www.renren.com/")
cookies = ""
for data in cookie:
    cookies = cookies + data.name + "=" + data.value + ";\t\n"
    print cookies