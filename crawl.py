<<<<<<< HEAD
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.head.script)
=======
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.head.title)
>>>>>>> 36a4b702351445ed74bb50572010fc5b2edd58ba
