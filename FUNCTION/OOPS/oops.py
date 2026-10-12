class Person:
    name = "Girija"
    town = "Nandyal"
    subject = "Maths"
    def info(self): 
        print(f"{self.name} is a {self.town}")
    
b = Person()
b.name ="Harry"
b.town = "mumbai"
print(b.name,b.town) 
a = Person()
print(a.name,a.town,a.subject)
a.info()
del a