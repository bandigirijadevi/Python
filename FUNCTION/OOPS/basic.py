class Person:
    name = "Girija"
    town = "Nandyal"
    subject = "Maths"
    def info(self): 
        print(f"{self.name} is a {self.town}")
    
 
a = Person()
print(a.name,a.town,a.subject)
a.info()