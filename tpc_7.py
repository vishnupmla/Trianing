def test(n):
    s=0
    if(n>0):
        for i in range(1,n+1):
            s=s+i
        
    return s

x=test(int(input('Enter a number: ')))
print('Number is - ',x*2)
        