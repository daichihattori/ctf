import string,random,itertools
import urllib.request,json
 
size = 8
url = 'https://jupiter.challenges.picoctf.org/problem/56816/'
id = 'pass'

chars = string.digits
 
# for ch in itertools.product(chars,repeat=size):
#     password = ''.join(ch)
#     print(password)

req = urllib.request.Request(url)
data = {
    'pass': "password",
}
headers = {
    'Content-Type': 'application/json',
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)
with urllib.request.urlopen(req) as res:
    body = res.read()