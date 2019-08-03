Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word='Hello'
>>> word
'Hello'
>>> reversed(word)
<reversed object at 0x00000193F6415A48>
>>> list
<class 'list'>
>>> list[word]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list[word]
TypeError: 'type' object is not subscriptable
>>> list(word)
['H', 'e', 'l', 'l', 'o']
>>> list(reversed(word))
['o', 'l', 'l', 'e', 'H']
>>> str1=''.join(reversed(word))
>>> str1
'olleH'
>>> def print_number(a,b,c):
	print(a)
	print(b)
	print(c)

>>> print_number(10,20,30)
10
20
30
>>> x=[10,20,30]
>>> x
[10, 20, 30]
>>> print_number(x)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print_number(x)
TypeError: print_number() missing 2 required positional arguments: 'b' and 'c'
>>> print_number(*x)
10
20
30
>>> 
