import urllib.request
import urllib.parse
import socket
import urllib.error

# Urlopen使用
response = urllib.request.urlopen("https://www.python.org")
#print(response.read().decode("utf-8"))
#print(type(response))

#print(response.status)
#print(response.getheaders())
#print(response.getheader("Server"))

# Data参数
data = bytes(urllib.parse.urlencode({"word":"hello"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
#print(response.read())

#TimeOut参数
try:
    response  = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("Time Out")


#Request
request = urllib.request.Request("http://python.org")
response = urllib.request.urlopen(request)
#print(response.read().decode("utf-8"))



