html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# from pyquery import PyQuery as pq
# doc = pq(html)
# # 初始化 字符串
# print(doc('li'))
# print('------')
# print(doc('a'))
# print('-----')
# print(doc('span'))

# 初始化一个url
# from pyquery import PyQuery as pq
# doc = pq(url='http://cuiqingcai.com')
# print(doc('title'))

# 初始化一个文件。
 
# from pyquery import PyQuery as pq
# doc = pq(filename='demo.html')
# print(doc('li'))

# 持续化集成
# 基本的css 选择器
html = '''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
 </div>
'''
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))
# 查找节点

from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
print('这个是用来查找子节点')
lis = items.children()
print(type(lis))
print(lis)


#  查找子节点中指定类型的节点
print('筛选节点')
lis = items.children('.active')
print(lis)

