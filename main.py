firstnumber=float(input("Enter your First Number: "))
function=str(input("Enter the (+,-,*)"))
secondnumber=float(input("Enter your Second Number: "))

if function=='+':
    output=firstnumber+secondnumber
elif function=='-':
    output=firstnumber-secondnumber
elif function=='*':
    output=firstnumber*secondnumber
    
print("Answer is: ",output)