# coding:utf-8
import jieba

mystr = "jieba分词器展示，以及效果呈现"
goat_list = jieba.cut(mystr,cut_all=True)
print goat_list # <generator object cut at 0x0000000009ADF048>
print "__"*20
print "/".join(goat_list)

goat_list = jieba.cut_for_search(mystr)
print "/".join(goat_list)