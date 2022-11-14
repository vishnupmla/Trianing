def factors(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    cnt=len(lst)    
    return cnt

x=factors(32)

print(x)
            

