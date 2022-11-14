#dictionary
#---------------------


a={ 'name': 'Vishnu', 'age':21, 'college':'CEC'}
#print(a['college'])
a['country']= 'India'
b=a.get('nation','India')
print(b)
print(a.items())
print(a.keys())
print(a)
print(a.pop('name'))
print(a.pop('name','Anwar'))

a.setdefault('Place','Chengannur')
#print(a)

b={'dob':'24-05-2000', 'number':1234567}
b.update(a)
print(b)






