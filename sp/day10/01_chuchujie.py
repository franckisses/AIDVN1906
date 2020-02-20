
import requests
import hashlib


url = 'http://seller.chuchujie.com/sqe.php?s=/AccountSeller/login'
headers = {'User-Agent':'Mozilla/5.0'}
s = hashlib.md5()
s.update('chuchuJIE123.'.encode())
data = {
    'username':'18667018590',
    'password': s.hexdigest(),
    'login_typy':'',
    'sms_code':'171604',
    'redirect_uri':'', 
    'channle': ''
} 
try:
    response = requests.post(url=url,data=data,headers=headers)
except Exception as e:
    print(e)
print(response.status_code)
print(response.text)
