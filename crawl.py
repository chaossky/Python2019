<<<<<<< HEAD
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.head.title)
=======
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.head.title)
>>>>>>> 18c0589cd863ddd50038bf9d112beb00982f3dfd
