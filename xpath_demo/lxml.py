# -*- coding: utf-8 -*-

import lxml
import lxml.etree


html = lxml.etree.parse("index.html")
res = html.xpath("//li")    # res是一个列表，包含所有li元素
html.xpath("//li/@class")   # 取出li的所哟u节点的class名称
html.xpath("//*[@class=\"3\"]") # 寻找text=3的元素
html.xpath("//*[@id=\"useful\"]/li/text()") # 取出所有id=useful下面的li标签的文本内容