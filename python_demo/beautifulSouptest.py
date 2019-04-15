from bs4 import BeautifulSoup

 # lxml解析器基础使用
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
#print(soup)

# 基本用法
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon atime there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a wll.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())
#print(soup.title.string)
#print(type(soup.title))
#print(soup.p.string)
#print(soup.head)
#print(soup.b.string)

#关联选择
print(soup.p.contents)