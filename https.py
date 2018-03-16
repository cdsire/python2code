# encoding:utf-8
import urllib2
import urlparse
import ssl


'''
def download(url):
    return urllib2.urlopen(url).read()  # python2没有文本与进制转换
    print download("https://www.baidu.com/")    # 不能处理加密风格
'''

context = ssl._create_unverified_context()  # 忽略安全
url = "https://www.baidu.com/"
headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request,context=context)
print response.read()


