import requests

# tarenacode
# code_2013

auth = ('tarenacode','code_2013')

response = requests.get(
    url='http://code.tarena.com.cn',
    auth = auth,
    headers = {
        'User-Agent':'Mozilla/5.0'
    }
)
print(response.text)


