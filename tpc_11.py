def armst(n):
    
    c=0
    a=len(n)
    for i in n:
        c=c + int(i)**a
    if int(n)==c:
        print('Armstrong')

    else:
        print('not armstrong')

armst(input('Enter a num'))


