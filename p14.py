n= int(input('Enter a number'))
flag=False
if n>1:
    for i in range(2,n):
        if(n%i)== 0:
            flag=True
            break
if flag==True:
    print('The number is not a prime number')

else:
    print('The number is a prime number')

