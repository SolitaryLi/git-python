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

from urllib import request, parse
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Host": "httpbin.org"
}
dict = {
    "name": "Germey"
}
data = bytes(parse.urlencode(dict), encoding="utf-8")
req = request.Request(url= url, data= data, headers= headers, method="POST")
response = request.urlopen(req)
#print(response.read().decode("utf-8"))


#quote , unquote
from urllib.parse import quote, unquote

keyWord = "壁纸"
url = "http://www.baidu.com/s?wd=" + quote(keyWord) #可以有效防止中文乱码，将中文字符转化为URL编码
print(url)
print(unquote(url))  #解码




