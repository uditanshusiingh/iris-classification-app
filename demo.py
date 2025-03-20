name=input("Enter name of student: ")
print("Hi ",name," Enter your marks subjectwise out of 100:")
while True:
    phy=int(input("Enter marks obtained in Physics : "))
    if(phy>100 or phy<0):
        print("invalid marks try again!")
    else:
        break
while True:
    chem=int(input("Enter marks obtained in chemistry : "))
    if(chem>100 or chem<0):
        print("invalid marks try again!")
    else:
        break
while True:
    eng=int(input("Enter marks obtained in english : "))
    if(eng>100 or eng<0):
        print("invalid marks try again!")
    else:
        break
while True:
    math=int(input("Enter marks obtained in mathematics : "))
    if(math>100 or math<0):
        print("invalid marks try again!")
    else:
        break
while True:
    bio=int(input("Enter marks obtained in biology : "))
    if(bio>100 or bio<0):
        print("invalid marks try again!")
    else:
        break
total=phy+eng+chem+math+bio
print(" ",name, "your total marks is :",total)
if(phy<30 or eng<30 or chem<30 or bio<30 or math<30):
    print("You Failed!")
elif(total>=450):
    print("Grade A")
elif(total<450 and total>=350):
    print("Grade B")
elif(total<350 and total>=250):
    print("Grade C")
else:
    print(" You failed!")