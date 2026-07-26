# conditional operator symbols > < >= <=  == !=
a = int(input("enter your age"))
print ("age is ",a)
# if else statement = conditional statement where only one statement can be true
if(a>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
# if space is removed the code get error its called as indentation error

appleprice = 245
budget = 200
b = int(input("enter your budget"))
print("apple price is ",appleprice)
print("budget is ",budget)
if(appleprice > budget):
    print("you can not buy apple")
elif(appleprice > 180):
    print("you can buy apple")
else:
    print("you can buy apple and banana")
    