# encoding:utf-8
import urllib2

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPHandler(debuglevel=1)#访问网络，输出调试信息

opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener) # 全局生效

response = urllib2.urlopen("http://www.renren.com/")
