#class_ex001.py
#TODO :이것은 2차원 벡터를 구현한것이다
#TODO: 기타 많은 함수를 구현해볼 필요가 있다.
#! 벡터는 방향과 크기를 가지는 물리량
#! 물론 수학적으로는 조금 다른 의미를 가질 수다
import math

class Vector2D:
    #! 생성자
    def __init__(self,x,y):
        self.x=x
        self.y=y
#! 더하기 메소드 ( + operator)
    def __add__(self,other_vec):
            return Vector2D(self.x+other_vec.x,self.y+other_vec.y)
#! 빼기 메소드구현 (- operator)
    def __sub__(self,other_vec):
        return Vector2D(self.x-other_vec.x,self.y-other_vec.y)
#! print() 메소드 구현 방법을 지정한다.
    def __str__(self):
        return "({},{})".format(self.x,self.y)
#! -오퍼레이터를 혼자 쓸때 음수값으로 바꾸기(부호바꾸기)
    def __neg__(self):
        #! 단순하게 리런값을 스트링으로 만들어 버리면 
        #! 노말라이징을 할수가 없기 때문에 객체로 리턴이 되도록 하였다
        #! 그러므로 주석으로 처리하면 단순한 스트링으로 리턴값이 출격이 되어 
        #! 버린다.
         #return "({},{})".format(-self.x,-self.y)
         return Vector2D(self.x*-1,self.y*-1)

   #! 벡터의 크기
    def norm(self):#정규화 리턴값은 실수값으로 반환
        return (self.x**2 + self.y**2)**0.5


       
    

v1=Vector2D(30,40)
v2=Vector2D(10,20)

#print('v1=',v1, "v2=",v2)
#print(v1.norm())
#print(type(v1))
#print(v2.norm())

v3=v1+v2
print("v1+v2 = ",v3)
#print(v3.norm())
print(type(v3))
v4=v1-v2
print('v1-v2 =',v4)
print(v4.norm())
v5=-v1
print("v5= ",v5)
print(type(v5.norm()))
    
    

        