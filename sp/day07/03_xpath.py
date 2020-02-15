

# text = '''
# <div>
#     <ul>
#         <a>this is test!</a>
#         <li class="item-0"><a href="link1.html">first item</a></li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-inactive"><a href="link3.html">third item</a></li>
#         <li class="item-1"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''

# 匹配所有节点：
# from lxml import etree
# html = etree.HTML(text)
# result = html.xpath('//*')

# print(result)
# print('一共有%d个节点'%len(result)) # html body

# 匹配指定的标签
# result = html.xpath('//li')
# print(result)
# print('一共有%d个节点'%len(result))


# 从网页的根去（html）匹配 
# result = html.xpath('/html/body/div/ul/li')
# print(result)
# print('一共有%d个节点'%len(result))

# 查找子节点
# result = html.xpath('//li/a')
# # '//a'
# print(result)
# print('一共有%d个节点'%len(result))


# 匹配所有的子节点​
# result = html.xpath('//ul//a') # 匹配子孙标签
# print(result)
# print('一共有%d个节点'%len(result))


# result = html.xpath('//ul/a') # 匹配子标签
# print(result)
# 匹配父节点以及属性  [@属性名=‘属性值’]
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result) # ['item-1'] 

# 属性匹配
# result = html.xpath('//li[@class="item-0"]')
# print(result)


# 匹配文本
# result = html.xpath('//li[@class="item-0"]/a/text()')
# print('文本内容为：',result)

# 匹配标签中的所有文本
# result = html.xpath('//li[@class="item-0"]//text()')
# print('所有文本是：',result)

# 属性匹配：
# result = html.xpath('//li/a/@href') # '//img/@src'
# print('a标签的href属性为：',result)


# contains函数使用
from lxml import etree
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

# lxml
# sudo pip3 install lxml
# pip3 list | grep 'lxml'
