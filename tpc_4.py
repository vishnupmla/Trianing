#set - Set never contains duplicate elements

#s={8,3,4,8,7,'abc'}
a=[1,2,3,1,2,3]
print(set(a))

print(list(set(a)))     # to sort and delete duplicate elements from a list we can use set 
                        # function and convert the set to a list
#print(s)