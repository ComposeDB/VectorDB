import numpy as np
import msgpack_numpy as msgpack_np

import requests
import msgpack
url = "http://localhost:8000/insert"

data = np.array([[1,2,3],[4,5,6]])

data = { 'hello' : ['world'] }

data = msgpack.packb(data)
headers = {
    'content-type': 'application/x-msgpack',
    'accept' : 'application/x-msgpack'
}

r = requests.post(url, data=data, headers=headers)
print(r.text)