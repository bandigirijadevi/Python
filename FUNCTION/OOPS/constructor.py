class Person:
    def __init__(self, n, c):
        print("I am a person")
        self.name = n
        self.Class = c
        print(f"my name is {self.name} and {self.Class}")

a = Person("hello", "2")
b = Person("any", "4")