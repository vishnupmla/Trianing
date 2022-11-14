class test:

    def __init__(self,a,b) -> None:
        print("The data on first class init function")
        self.a=a
        self.b=b
        self.c=a+b

    def sum(self):
        print("sum = ",self.c)

class find(test):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
        test.__init__(self,a,b)

        print("a =",self.a)
        print("b=",self.b)

ob1= test(10,20)
ob2=find()
ob2.sum()





        
    