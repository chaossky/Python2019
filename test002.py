a=[]
for i in range(10):
    a.append(i)

print(a)

b=list(range(1,5))

print(b)

c=list(map(lambda n:n*n*n,b))

print(c)

f=list(filter(lambda n:n%2==0,b))
print(f)

from functools import reduce 
r=reduce(lambda n,m:n*m,b)
print(r)
