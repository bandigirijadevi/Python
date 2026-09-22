#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.

marks = [85, 90, 78, 92, "Harry"]
print(marks)
print(marks[0])
print(marks[1])

print(marks[-3])
print(marks[1:-1])
print(marks[5-3])
print(marks[len(marks)-3])
print(marks[1:4:2])