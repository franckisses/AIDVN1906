
# csv 模块
import csv

with open('test.csv', 'a', encoding='utf-8') as f:
    wirter = csv.writer(f)
    # 写入一行的方法
    wirter.writerow(['武汉','加油'])
    # 写入多行
    wirter.writerows([('中国','北京'),('美国','华盛顿'),('德国','柏林')])

# TODO 将猫眼电影存到csv中