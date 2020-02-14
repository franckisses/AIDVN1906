
# from urllib import request
# # 第一种保存文件的方式
url = 'http://2sc2.autoimg.cn/escimg/g26/M07/5F/2E/f_900x675_0_q87_autohomecar__ChsEe14f2P6AQazvAAHPOvAyLGo064.jpg'
# res = request.urlopen(url)
# html = res.read()
# with open('car.jpg','wb') as f:
#     f.write(html)


# 第二种保存文件的方式
from urllib import request
try:
    result = request.urlretrieve(url,'nihao/baidu/my_car_bak.jpg')
except Exception as e:
    print(e)
else:
    print('文件下载完成',result)

