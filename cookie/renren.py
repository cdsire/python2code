# encoding:utf-8
import urllib2
import cookielib
import urllib


# 创建一个对象存储cookie
cookie = cookielib.CookieJar()
# 创建一个链接对象使用cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
# 创建打开器，使用cookie
opener = urllib2.build_opener(cookie_handler)
# 增加一个浏览器模拟
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
loginurl = "http://www.renren.com/PLogin.do"
data = {"email":"625280424@qq.com","password":"cdsire0124"}
# 编码
data = urllib.urlencode(data)
# post请求登录，抓取cookie
request = urllib2.Request(loginurl,data=data)
# 抓取cookie，登录
response = opener.open(request)
response_index = opener.open("http://www.renren.com/374309806")
print response_index.read()
