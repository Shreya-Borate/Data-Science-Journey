class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):
        Ans = self.No1 - self.No2
        return Ans
    



print("Enter 1st num : ")
no1 = int(input())

print("Enter 2nd num : ")
no2 = int(input())

Aobj = Arithmatic(no1,no2)


Ret = Aobj.Addition() 
print("Addition is : ",Ret)

Ret = Aobj.Subtraction() 
print("Subtraction is : ",Ret)