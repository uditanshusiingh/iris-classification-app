num = int(input("Enter number1 : "))
num1 = int(input("Enter number2 : "))
num2 = int(input("Enter number3 : "))

if(num>num1 and num>num2):
    print(num," is greater among these.")
elif(num1>num and num1>num2):
    print(num1," is greater among these.")
else:
    print(num2," is greater among these.")
