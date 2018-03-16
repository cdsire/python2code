# -*- coding: utf-8 -*-
import urllib
import urllib2
import re


# 抓取python贴吧关注人数和页面数量信息peoplenumbers,tienumbers
def gettiebalistnumbers(name):
    headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    url = "http://tieba.baidu.com/f?"   # 贴吧首页url，留下？后面的接口用来拼接
    word = {"kw":name}  # 贴吧的名字
    word = urllib.urlencode(word)   # 编码成字符串
    url = url + word    # 拼接url
    request = urllib2.Request(url,headers=headers)  # 发起请求
    # 添加/修改一个特定的header
    request.add_header("Connecion","keep-alive")    # 一直活着
    response = urllib2.urlopen(request)
    data = response.read()

    # 抓取关注人数
    restr = "<span class=\"card_menNum\">([\s\S]*?)</span>"  # 帖子数的正则表达式
    regex = re.compile(restr, re.IGNORECASE)  # 预编译
    mylist = regex.findall(data)  # 正则抓取页面所有符合条件的值
    peoplenumbers = mylist[0].replace(",", "")  # 去掉帖子数的分隔符
    peoplenumbers = eval(peoplenumbers)  # 转化为整数

    # 抓取帖子数量
    restr = "<span class=\"card_infoNum\">([\s\S]*?)</span>"    # 帖子数的正则表达式
    regex = re.compile(restr,re.IGNORECASE) # 预编译
    mylist = regex.findall(data)    # 正则抓取页面所有符合条件的值
    tienumbers = mylist[0].replace(",","") # 去掉帖子数的分隔符
    tienumbers = eval(tienumbers) # 转化为整数
    return peoplenumbers,tienumbers # 关注人数/帖子数

# 提取百度贴吧每一页的连接
def gettiebalist(name):
    numbertuple = gettiebalistnumbers(name)
    tienumbers = numbertuple[1]
    tiebalist = []
    if tienumbers % 50 ==0:
        for i in range(tienumbers // 50):
            tiebalist.append("http://tieba.baidu.com/f?kw="+name+"&pn="+str(i*50)+"")
    else:
        for i in range(tienumbers // 50 + 1):
            tiebalist.append("http://tieba.baidu.com/f?kw="+name+"&pn="+str(i*50)+"")
    return tiebalist

# 提取每一页的子链接的子链接
def geturllistfrompage(url):
    headers= {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    data = response.read()

    restr = "<ul id=\"thread_list\" class=\"threadlist_bright j_threadlist_bright\">([\s\S]*?)<div class=\"thread_list_bottom clearfix\">"
    regex = re.compile(restr,re.IGNORECASE)
    mylist = regex.findall(data)
    tablestr = mylist[0]

    # 取出子链接的部分
    restr = "href=\"/p/(\d+)\""
    regex = re.compile(restr,re.IGNORECASE)
    urltitlelist = regex.findall(tablestr)

    # 合成子链接的url
    urllist = []
    for title in urltitlelist:
        urllist.append("http://tieba.baidu.com/p/" + title)
    return urllist

# 提取页面内容
def getpagedata(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    data = response.read()
    return data

# 提取页面中的邮箱
def getemaillistformpage(pagedata):
    restr = r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})" # 邮箱的正则表达式
    regex = re.compile(restr, re.IGNORECASE)
    emaillist = regex.findall(pagedata)
    return emaillist

# 提取页面中的qq
def getqqlistformpage(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    qqlist = []
    while True:
        line = response.readline()
        if not line:
            break
        if line.find("QQ") != -1 or line.find("Qq") != -1 or line.find("qq") != -1:
            restr = "[1-9]{5,10}"
            regex = re.compile(restr,re.IGNORECASE)
            templist = regex.findall(line)
            qqlist.extend(templist)
    return qqlist

# 抓取python贴吧关注人数和页面数量信息peoplenumbers,tienumbers
# print gettiebalistnumbers("python")

# 提取百度贴吧每一页的连接
# mylist = gettiebalist("python3")
# for pageurl in mylist:
#     print pageurl

# 提取每一页的子链接的子链接
# mylist = gettiebalist("water")
# for subpageurls in mylist:
#         sub_url_list = geturllistfrompage(subpageurls)  # 每一页的打印结果都是一个列表
#         print sub_url_list

# 提取页面中的邮箱
# sub_urls = []
# mylist = gettiebalist("water")
# for subpageurls in mylist:
#     sub_url_list = geturllistfrompage(subpageurls)  # 每一页的打印结果都是一个列表
#     sub_urls.extend(sub_url_list)
# # print sub_urls
# # print len(sub_urls)
# for url in sub_urls:
#     all_pagecontent_list = getpagedata(url)
# for pagecontent in all_pagecontent_list:
#     print getemaillistformpage(pagecontent)




# 提取页面中的qq
# print getqqlistformpage("http://tieba.baidu.com/p/5574733761")
sub_urls = []
mylist = gettiebalist("water")
for subpageurls in mylist:
    sub_url_list = geturllistfrompage(subpageurls)  # 每一页的打印结果都是一个列表
    sub_urls.extend(sub_url_list)
# print sub_urls
# print len(sub_urls)
for url in sub_urls:
    print getqqlistformpage(url)