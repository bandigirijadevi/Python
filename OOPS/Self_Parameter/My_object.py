class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class: