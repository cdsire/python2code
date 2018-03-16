# coding:utf-8
import jieba    # 分词
import matplotlib.pyplot as plt    # 数据可视化
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS   # 词云
import numpy as np  # 科学计算
from PIL import Image   # 处理图片


# 打开文本
textfile = open("rsa.txt").read()   # 读取所有文本
wordlist = jieba.cut_for_search(textfile) # 切割
space_list = " ".join(wordlist)  # 连接词语
background = np.array(Image.open("1.png"))  # 背景图片
mywordcloud = WordCloud(background_color="black",   # 背景颜色
                        mask=background,    # 写字用的背景图片，从背景图提取颜色
                        max_words=20,   # 最大词语数量
                        stopwords=STOPWORDS,    # 从哪停止
                        font_path="simkai.ttf", # 字体路径，使用默认的“simkai.ttf”
                        max_font_size=200,  # 最大是字体的尺寸
                        random_state=50,    # 随机角度，有的是斜着，有的横着
                        scale=2 # 放大或者缩小
                        ).generate(space_list)  # 生成词云

image_color=ImageColorGenerator(background) #生成词云的颜色
plt.imshow(mywordcloud) #显示词云
plt.axis("off") #关闭保存
plt.show()

