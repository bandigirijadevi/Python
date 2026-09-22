class Person:
    name = 'Harry'
    occupation = 'Software develper'
    networth = 10000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
A = Person()
b = Person()
b.name = 'Richa'
print(A.name)
A.info()
b.info()