#program to find factors of numbers

def factn(n):
    
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
    
factn(32)
factn(54)


