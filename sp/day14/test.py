
import json

test_list = [
    {'name':'xiaowang','age':12},
    {'name':'xiaowang','age':12},
    {'name':'xiaowang','age':12}
]
for i in test_list:
    with open('test2.json','a') as f:
        json.dump(json.dumps(i)+'\r\n',f)