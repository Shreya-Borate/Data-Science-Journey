class Arithmatic:
    def Addition(self,No1,No2):
        Ans = No1 + No2
        return Ans

    def Subtraction(self,No1,No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithmatic()

print("Enter 1st num : ")
no1 = int(input())

print("Enter 2nd num : ")
no2 = int(input())

#Ret = Addition(Aobj,no1,no2)
Ret = Aobj.Addition(no1,no2) 
print("Addition is : ",Ret)

Ret = Aobj.Subtraction(no1,no2) 
print("Subtraction is : ",Ret)