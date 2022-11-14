p=int(input('Enter the principal amount '))
r=int(input('Enter the rate of interest \t'))
t=int(input('Enter the time'))

r= r/100
a=p*(1+r*t)
print("Total amount after 3 year is \t", a)

i= (a-p)/t
print('Interest per annum is\t',i)