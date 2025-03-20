hyp = float(input("Enter value : "))
height = float(input("Enter value : "))
base = float(input("Enter value : "))

# if(hyp>height and hyp>base):
if((hyp**2) == (height**2) + (base**2)):
        print("It is a right angled triangle.")
# elif(hyp<height and height>base):
elif((height**2) == (hyp**2) + (base**2)):
        print("It is a right angled triangle.")
# elif(base>height and hyp<base):
elif((base**2) == (height**2) + (hyp**2)):
        print("It is a right angled triangle.")
else:
    print("It is not a right angled triangle.")
