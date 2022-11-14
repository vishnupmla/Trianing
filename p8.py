#Leap Year
from datetime import date

t=date.today().year
y=int(input("Enter the year"))
if(y<t):
    print("Please enter a year greater than the current year")

print("The leap years are:")
for i in range(t,y):
    if(i%4==0):
        print(i)

    
     

    