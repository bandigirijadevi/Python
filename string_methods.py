'''
len() = length of string
upper() = converts string into uppercase
concept of immutability
strings are immmutable
lower[] = convert string t lowercase
rstrip[] = removes any trailing characteristics
replace = replace the occurenece of string into the other string
splits = given string at the specalized instance and returns the seperated strings as list items
capatilize = first letter of the string into the uppercase and rest other to the lowercase
centre = it align the string to centre as per the parameters
count = counts the number of occurences of a string in the given string
endwith = checks whether the string ends with the specified value like true or false
'''
a = "ram !!!!! !!!!!! !!!!!!!! !!!!!!"



print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.split(" "))
print(a.capitalize())

heading = "welcome to python"
print(heading.capitalize())

blogHeading = "welcome to c"
print(len(blogHeading))
print(len(blogHeading.center(20)))
print(a.count("!"))
print(a.endswith("ram"))



