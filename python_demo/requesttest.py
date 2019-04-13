import requests

# 基本用法
r = requests.get("http://www.baidu.com")  #注：要写明http or https
#print(type(r))
#print(r.status_code)
#print(r.text)
#print(r.cookies)

#正则表达式
import re
content = "Hello 1234567 World_This is a Regex Demo 7896"
result = re.match("^Hello\s(\d+)\sWorld", content)
print(result)
print(result.group())
print(result.group(1))

#正则表达式 通用 Or 贪婪 or 非贪婪
content = "Hello 123 4567 World_This is a Regex Demo"
result = re.match("He.*Demo$", content)  #.* 匹配任意字符
print(result)
print(result.group())

result = re.match("He.*(\d+).*Demo$", content)
print(result)
print(result.group())
print(result.group(1))

result = re.match("He.*?(\d+)\s(\d+).*Demo$", content)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))





