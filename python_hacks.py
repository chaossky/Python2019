Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a,b=5,10
>>> print(a,b)
5 10
>>> a,b=b,a
>>> print(a,b)
10 5
>>> a=["Python","is","awesome"]
>>> print(" ",join(a))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(" ",join(a))
NameError: name 'join' is not defined
>>> print(" ".join(a))
Python is awesome
>>> a=[1,2,3,1,2,3,2,2,4,5,1]
>>> print(max(set(a),key=a.count))
2
>>> from collections import Counter
>>> cnt=Counter(a)
>>> print(cnt.most_common(3))
[(2, 4), (1, 3), (3, 2)]
>>> 
