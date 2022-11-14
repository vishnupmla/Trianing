number = input("Enter a number")
a = len(number)
arm = 0
for i in number:
    arm = arm + int(i)**a

if (arm == int(number)):
    print("the number is an Armstrong number")

else:
    print("The number is not a armstrong number")
