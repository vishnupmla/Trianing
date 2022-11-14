num=int(input('Enter the range'))
f1=0
f2=1
for i in range(0,num):
    f=f1+f2
    f1=f2
    f2=f
    print(f)
    
    

