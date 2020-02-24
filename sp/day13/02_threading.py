# 导入模块
from threading import Thread

# 使用流程  
t = Thread(target=函数名,) # 创建线程对象
t.start() # 创建并启动线程
t.join()  # 阻塞等待回收线程

# 如何创建多线程？？？？？？
t_list = []

for i in range(10):
    t = Thread(target=函数名)
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()