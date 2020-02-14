"""
 以下内容是对于文件的操作：
"""

import os  # operation system
# 1  判断操作平台
print('当前的操作平台是：',os.name) 
# posix linux
# nt windows
# 2.显示当前脚本的工作路径 
print(os.getcwd())  # 返回值是当前的工作文件夹的位置 

# 3. 列出当前文件加下的所有文件和目录
print('day06中的文件和文件夹包括：',
os.listdir('/Users/gongyan/Desktop/AIDVN1906/sp/day06'))
# 4.删除一个文件
# print('删除文件jpg',os.remove('my_car_bak.jpg'))
# 5.生成多层目录
# os.makedirs('haha/xixi/hehe/wuwu')
# 判断文件夹是否存在
print(os.path.isdir('haha'))
# 判断文件是否存在 
print(os.path.isfile('cautions.txt'))
