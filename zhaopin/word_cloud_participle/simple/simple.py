#coding:utf-8
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# 读取全部文件的内容
text = open(path.join(d, '3.txt'),"rb").read()  #rb二进制读取，
text=text.decode("utf-8") #按照utf-8解码
print text #utf-8
# Generate a word cloud image，根据词语创建云图
wordcloud = WordCloud(font_path="simkai.ttf").generate(text)

# Display the generated image:
# the matplotlib way:

import matplotlib
import  matplotlib.pyplot as plt #数据可视化

matplotlib.rcParams["font.sans-serif"]=["simhei"] #配置字体
matplotlib.rcParams["font.family"]="sans-serif"

#绘图1
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
#绘图2
wordcloud = WordCloud(width=800, height=400,font_path="simkai.ttf",max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()
