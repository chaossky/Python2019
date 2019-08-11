a,b=5,10
print(a,b)
#5 10
a,b=b,a
print(a,b)
#10 5
a=["Python","is","awesome"]
print(" ",join(a))
print(" ",join(a))
print(" ".join(a))
a=[1,2,3,1,2,3,2,2,4,5,1]
print(max(set(a),key=a.count))
#2
from collections import Counter
cnt=Counter(a)
print(cnt.most_common(3))
#[(2, 4), (1, 3), (3, 2)]

