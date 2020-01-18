import requests
import random
import threading

def getPage():
    url = 'http://127.0.0.1:8000/v1/users/test'
    url1 = 'http://127.0.0.1:8001/v1/users/test'
    current_url = random.choice([url,url1])
    requests.get(current_url)


ts = []
for i in range(30):
    t = threading.Thread(target=getPage)
    ts.append(t)

if __name__ == "__main__":
    for i in ts:
        i.start()

    for i in ts:
        t.join()
