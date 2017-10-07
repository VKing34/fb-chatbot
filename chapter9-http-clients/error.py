
from urllib.request import urlopen
import urllib.error
import requests

# try:
#     r = urlopen('http://httpbin.org/status/500')
# except urllib.error.HTTPError as e:
#     print(e.status, repr(e.headers['Content-Type']))
#
# x = requests.get('http://httpbin.org/status/500')
# print(x.status_code)
# x.raise_for_status()

r = requests.get('http://httpbin.org/headers')
print(r.text)

s = requests.session()
s.headers.update({'Accept-Language': 'en-US,en;q=0.8'})

print(s.headers)
s.get('http://httpbin.org/headers')
