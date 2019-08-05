def findNearestSquareNumber(n):
    temp=0
    if n**2>temp:
        print ('%s' % n**2)
        
    if (n+1)**2>temp:
        print (n)

for i in range(10):
    print(findNearestSquareNumber(i))


