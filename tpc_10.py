def prime(n):
    flag=False
    for i in range(2,n):
        if(n%i==0):
            flag=True
            break
    if (flag==True):
        print('The number is not prime')
    else:
        print('The number is prime')

prime(29)
    