#b='Anwar'
#b[2]='z'
#print(b) 
#string cannot be changed like list elements using direct assignment, use replace()
#a=[10,20,'abc',15,35,15]
#a[5]=20
#---------------------
#pop(position) [return the popped element]
#remove(value) [Removes first  occurance of value]


a=[10,20,'abc',15,35,15]
#a[5]=20
a.append(20)
a.append('Anwar')
#a.extend('anwar')
#print(a)

c=[5,1,3,10]
#c.sort(reverse=True)
c.insert(2,13)
print(c)
c.pop(3)
print(c)

print(a)
a.remove(15)
print(a)
