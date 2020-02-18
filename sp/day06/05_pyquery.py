html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print(items)
# print('-----\n',type(items))

# container = items.parent()
# print(type(container))
# print(container)
# 找祖先节点
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)


# 在所有祖先节点中选择出某一个
print('\n')
parent = items.parents('.wrap')
print(parent)