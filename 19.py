def armstr(n):
    num=n
    size=len(str(n))
    c=0
    while(num!=0):
        a=num%10
        c=c+a**size
        num=num//10
        # if num==0:
        #     break
    if c==n:
        print('Armstrong')
    else:
        print('Not armstrong')

    
armstr(153)