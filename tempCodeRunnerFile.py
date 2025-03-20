# without parameter
# def fun():
#     print("Hello World!")
# fun()

# with parameter
# def fun(a,b):
#     print(a+b)
# fun(10,20)

# def name(a):
#     print(a + " Singh")
# name("Uditanshu")

# keywords
# def name(a,b=10,c=2):
#     print(a+b+c)
# name(23)
# name(12,30)
# name(12,10,11)

# Prime number
num = int(input("Enter starting : "))
num1 = int(input("Enter limit : "))

for c in range (num,num1+1,1):
    for d in range (2,num1,1):
        if(c%d == 0):
            break
    if(c==d):
        print(c)

# language = 'PYTHON'
# # iterate over each character in language
# for x in language:
#  print(x)


# list = ["how", "are", "you"]
# for x in range(len(list)):
#     print(list[x])


# digits = [0, 1, 5]
# for i in digits:
#     print(i)
#     # if(i==1):
#     #     break
# else:
#     print("No items left.")



