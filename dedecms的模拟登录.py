# encoding:utf-8
import urllib2
import urllib
import cookielib # 有了cookielib才能模拟登录

url1 = "http://v57.demo.dedecms.com/dede/login.php?gotopage=%2Fdede%2Findex.php"
url2 = "http://v57.demo.dedecms.com/dede/index.php"

jar = cookielib.LWPCookieJar()
cookieprocessor = urllib2.HTTPCookieProcessor(jar)
opener = urllib2.build_opener(cookieprocessor,urllib2.HTTPHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen(url1)

PostData = {
    "dopost": "login",
    "adminstyle": "newdedecms",
    "userid": "admin",
    "pwd": "admin",
    "sm1": "",
}
PostData = urllib.urlencode(PostData)
headers = {
            'Referer':'http://v57.demo.dedecms.com/dede/login.php?gotopage=%2Fdede%2Findex.php',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'
}

request = urllib2.Request(url1,PostData,headers)
responsenew = urllib2.urlopen(request)
print responsenew.read()

print "-----------------------------------"
print "-----------------------------------"

responsenew2 = urllib2.urlopen(url2)
print responsenew2.read()