def sum(n):
    total = 0
    i = 1
    while i<=n:
        total = total + i
        i = i +1
        
    return total
n = int(input("enter n :"))
print('Sum is :',sum(n))