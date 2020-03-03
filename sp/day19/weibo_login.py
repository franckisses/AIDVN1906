


import execjs
with open('./weibo.js','r') as f:
    weibo = f.read()

pattern = execjs.compile(weibo)

sp = pattern.eval('get_sp()')
print(sp)