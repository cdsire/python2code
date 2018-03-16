#encoding:utf-8
import matplotlib
import matplotlib.pyplot as plt
import selenium
import selenium.webdriver
import re

# 配置字体
matplotlib.rcParams["font.sans-serif"] = ["simhei"]
matplotlib.rcParams["font.family"] = "sans-serif"

def getnumberbyname(searchname):
    url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw="+searchname+"&sm=0&p=1"
    # 调用谷歌浏览器
    driver = selenium.webdriver.Chrome()
    # 访问链接
    driver.get(url)
    # 抓取网页源代码
    pagesource = driver.page_source
    # 职位数量的正则表达式
    restr = "<em>(\\d+)</em>"
    regex = re.compile(restr,re.IGNORECASE)
    mylist = regex.findall(pagesource)
    driver.close()
    return mylist[0]

pythonlist = [u"python",u"python 运维",u"python 测试",u"python 数据",u"python web"]
num = 0
for profession in pythonlist:
    num += 1
    print profession,eval(getnumberbyname(profession))
    plt.bar([num],eval(getnumberbyname(profession)),label=profession)

plt.legend()    # 绘制
plt.savefig("python_work.png")


