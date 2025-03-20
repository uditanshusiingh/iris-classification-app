temp = float(input("Enter temperature : "))
choice = int(input("Enter 1 for celsius and 2 for farenheit : "))

if(choice == 1):
    print("Temperature in celsius : ",(5*(temp-32))/9)
elif(choice == 2):
    print("Temperature in farenheit : ",(9*temp+160)/5)
else:
    print("Invalid choice.")