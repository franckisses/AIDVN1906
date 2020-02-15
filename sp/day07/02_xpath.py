from lxml import etree


html = etree.parse('./demo.html', etree.HTMLParser())
result = etree.tostring(html)
print('this is result:\n',result)
print(result.decode('utf-8'))


# 解析字符串 etree.HTML()
# 解析文档  etree.parse()

