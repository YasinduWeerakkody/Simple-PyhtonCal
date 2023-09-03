#python program to make simple calculator using function
def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)

no1=int(input("Enter First Number: "))
no2=int(input("Enter Second Number: "))

print("Select the option")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

while(True):
    choice=int(input("Select the Option: 1-2-3-4-5: "))
    if choice in(1,2,3,4,5):
        if choice==1:
            print("Addition two number",no1,"and",no2,"is: ",add(no1,no2))
        if choice==2:
             print("Subtraction two number",no1,"and",no2,"is: ",sub(no1,no2))
        if choice==3:
             print("Multiplication two number",no1,"and",no2,"is: ",mul(no1,no2))
        if choice==4:
             print("Divution two number",no1,"and",no2,"is: ",div(no1,no2))
        if choice==5:
            print("Thank you!")
            exit()
    else:
        print("Not valid try again")
        continue