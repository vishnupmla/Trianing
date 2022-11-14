def test(n):
    s=0
    i=1
    while(i<n+1):
        s=s+i
        i=i+1

    return s

x=test(int(input("Enter a number: ")))
print("SUm of number * 2 = ",x*2)
