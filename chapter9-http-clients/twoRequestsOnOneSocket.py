import http.client

h = http.client.HTTPConnection('httpbin.org:80')
h.request('GET', '/ip')
r = h.getresponse()
print(r.status)

h.request('GET', '/user-agent')
x = h.getresponse()
print(x.status)