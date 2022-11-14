print('Let''s check how the functions work\n')

def length(a=input('Enter the word\t')):
    
    try:
        a=int(a)
        print('Value is numeric')
        
    except:
        b=max(a)
        print(b)
        print('Normal')
    

print('The functions execute here \n')

length()