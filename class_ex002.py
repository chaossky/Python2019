# Super Class Person을 지정
class Person:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

    def name(self):
        return self.firstName+" "+self.lastName
        
#! 자녀 클래스 Employee와 Employer를 작성
class Employer(Person):
   
    def __init__(self,firstName,lastName,position):
        Person.__init__(self,firstName,lastName)
        self.position=position

    def info(self):
        return "Employer : "+self.name()+", "\
            +self.position

class Employee(Person):
   
    def __init__(self,firstName,lastName,staffID):
        Person.__init__(self,firstName,lastName)
        self.staffID=staffID

    def info(self):
        return "Employee : "+self.name()+", "\
            +str(self.staffID)

# 클래스의 인스턴스를 생성
worker=Employee("Sherlock","Gmones",1111)
cfo=Employer("James","Kim","CFO")

#인스턴스의 내용을 출력
print(worker.info())
print(cfo.info())

    


