#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#adding item to the list we use the append() function
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#The insert() method inserts an item at the specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# to add two list we use the extend method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#extend method also can add tuples set and dictonaries
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)