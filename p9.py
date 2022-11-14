#Program to print group of +ve numbers from a list

list=[]

n=int(input(("enter the number of elements to be stored in list")))
print("Enter the list of elements")
for i in range(0,n):
    list.append(int(input()))

print("The positive integers are :")
for i in list:
    if(i>0):
        print(i)

