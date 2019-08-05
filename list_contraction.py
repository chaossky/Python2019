#리스트 축약

#1
#0,1,2,3,4를 가지는 리스트를 선언해 보자

list1 = [x for x in range(5)]
print(list1)

#2
#0.5를 곱한
list2=[0.5*x for x in range(5)]
print(list2)

list3=[0.5*x for x in list1]
print(list3)

#3
#조건을 달아서 1.5미만만 골라 리스트 생성

list4=[x for x in list3 if x<=1.5]
print(list4)

#조건을 달아서 홀수 (2로 나누어 나머지가 1인것)리스트 생
list5=[x for x in range(20) if x%2==1]
print(list5)

list6=[i for i in range(100) if i%3==0]
print(list6)



