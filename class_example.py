# * class_example
# ! 경고 / 주의 initialize class
# ? 물음
# TODO
# @PARAM self 
 

class Human:
    def __init__(self,age=0,gender="Male",name="Unknown"):
        self.age=age
        self.gender=gender
        self.name=name

    def __str__(self): 
        if self.gender=="Male":
            pronoun="He"
        else:
            pronoun="She"   

        return "This is {}. {} is {} years old.".format(self.name, pronoun,self.age)

p1=Human(10,"Male","John")
print(p1)

p2=Human(15,"Female","Susan")
print(p2)

print(dir(p1))

    
