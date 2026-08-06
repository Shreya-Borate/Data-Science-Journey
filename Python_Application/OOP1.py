class Demo:
    #class variables
    Value1 = 10
    Value2 = 20

    def __int__(self):
        self.No1 = 11
        self.No2 = 21

    #Instance Method
    def fun(self):
        print("Inside Instance Method named as Fun")
        print(self.No1)
        print(self.No2)

        print(self.Value1)
        print(self.Value2)

Dobj = Demo()
Dobj.fun()