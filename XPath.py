# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  XPath.py
    Description:
    Author:     Administrator
    Date:       2020/03/03
    Time:       21:27
-------------------------------
    Modify Activity:
                2020/03/03
-------------------------------
"""
__author__ = 'Administrator'


from lxml import etree
import pprint

text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
"""

html = etree.HTML(text)         # 构造了一个XPath解析对象，其中会自动修正HTML文本
# result = etree.tostring(html)       # 输出修正后的HTML代码，结果是byte类型
# result = result.decode('utf-8')     # decode()方法把结果转为utf-8类型

nodes = html.xpath('//ul/a')
pprint.pprint(nodes)

