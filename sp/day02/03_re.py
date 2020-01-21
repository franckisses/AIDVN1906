import re

s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))
# 结果: ['A B','C D']
p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))
# 第1步:匹配完整 -> ['A B','C D']
# 第2步:匹配()中 -> ['A','C']

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))
# 第1步:匹配完整 -> ['A B','C D']
# 第二步 [('A','B'),('C','D')]
# 9:08 