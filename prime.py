# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if(n%i==0):
#             count=count+1
           
#     if (count>2):
#         print('The number is not prime')
#     else:
#         print('The number is prime')

# prime(22)

def prime(n):
    flag='not_prime'
    for i in range(2,n):
        if(n%i==0):
            flag='Prime_number'
            break
    return flag

x=prime(29)
print(x)
    
    