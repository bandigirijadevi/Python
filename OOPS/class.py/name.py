class Students:
    def __init__(self,name,age,education): # this method is called contstructor
        self.name = "girija"
        self.age = 20
        self.education = 13
    
    def math(self):
        print("my name is ", self.name)
        print("my age is ", self.age)   # instance method
        print("my education is ",self.education)

s1 = Students("girija",12,13)
s1.math()

s2= Students("gira",12,13)
s2.math()