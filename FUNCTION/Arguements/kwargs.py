#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")