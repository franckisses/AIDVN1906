
import requests
# verify = True (默认检查证书)
# verify = False  忽略检查证书

# 示例
response = requests.get('https://www.12306.cn', verify=False)
print(response.text)

