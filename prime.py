# num = int(input("Enter starting : "))
num1 = int(input("Enter limit : "))

for c in range (1,num1+1,1):
    for d in range (2,num1,1):
        if(c%d == 0):
            break
    if(c==d):
        print(c)