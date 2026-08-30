def my_name(lastname): # lastname is the parameter
 print(lastname +  " Ram")

my_name("Goutham") #Goutham is the argument
my_name("Linus")
#A parameter is the variable listed inside the parentheses in the function definition
#An argument is the actual value that is sent to the function when it is called.

#NUMBEER OF ARGUEMENTS
#a function must be called with the correct number of arguments

#If your function expects 2 arguments, you must call it with exactly 2 arguments.

def vechile(Type , Cost):
 print(Type,Cost)
 
vechile("NANO",130000)

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")