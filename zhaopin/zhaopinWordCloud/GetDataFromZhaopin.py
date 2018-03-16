# encoding:utf-8
import selenium
import selenium.webdriver
import re
import urllib2
import urllib


# 获取深圳的职位页的url
def geturllistsz(searchname):
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=" + searchname + "&p=1&isadv=0"
    # 调用谷歌浏览器
    driver = selenium.webdriver.Chrome()
    # 访问链接
    driver.get(url)
    # 抓取网页源代码
    pagesource = driver.page_source
    # 正则表达式
    restr = "<em>(\\d+)</em>"
    # 预编译正则表达式
    regex = re.compile(restr, re.IGNORECASE)
    # 提取正则表达式的内容列表
    mylist = regex.findall(pagesource)
    driver.close()
    # 获取职位数量的整数形式
    num = eval(mylist[0])

    # 根据岗位数量求总共的页数
    if num % 60 == 0:
        pages = num // 60
    pages = num // 60 + 1

    # 每一页的链接构成的列表
    mylist = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=f99ca7fb8471433c9d30016b26188c7b&p=" + str(i) for i in range(1, pages + 1)]
    for page_url in mylist:
        print page_url
    return mylist

def downloadgeturllist(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"
    }
    request = urllib2.Request(url,headers=headers)
    # 也可以通过调用request.add_header()添加/修改一个特定的header
    request.add_header("Connection","keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()



