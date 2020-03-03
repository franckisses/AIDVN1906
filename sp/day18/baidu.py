import execjs


# nodejs
# pyexecjs
# pyexecjs

with open('./translate.js','r') as f:
    js = f.read()

pattern = execjs.compile(js)
sign = pattern.eval("e('sign')")

print('sign',sign)
#window.bdstoken = 'b25783d90e19bb9db9c46f5fbefb10b2';
# window.gtk = '320305.131321201';

# window.bdstoken = 'b25783d90e19bb9db9c46f5fbefb10b2';
# window.gtk = '320305.131321201'



