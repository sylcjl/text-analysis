#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymysql
from lxml import etree
import requests
import nltk
import jieba
import jieba.analyse
from snownlp import SnowNLP

jieba.set_dictionary("dict.txt.big.txt")
jieba.load_userdict("user_dict.txt")


# url = 'http://www.appledaily.com.tw/realtimenews/article/life/20160125/782931/'
# response = requests.get(url)
# tree = etree.HTML(response.content)

# title = tree.xpath('//h1[@id="h1"]')[0].text
# articleContent = ' '.join(i.xpath('normalize-space()') for i in tree.xpath('//div[@class="articulum trans"]'))

# seg_list = jieba.cut_for_search(articleContent, HMM=True)


## test frequency tune
testlist = [
(u'今天天气不错', (u'今天', u'天气')),
(u'如果放到post中将出错。', (u'中', u'将')),
(u'我们中出了一个叛徒', (u'中', u'出')),
]

for sent, seg in testlist:
    print(SnowNLP(sent).sentiments)
    print(u'/'.join(jieba.cut(sent, HMM=False)))
    word = ''.join(seg)
    print(u'%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
    print(u'/'.join(jieba.cut(sent, HMM=False)))
    print(u"-"*40)
