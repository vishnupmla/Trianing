word=input("enter the word")
vowels="aeiouAEIOU"
for i in word:
    for j in vowels:
        if(i== j):
            print(i)
