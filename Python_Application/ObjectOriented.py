class Arithmatic:
    def Addition(No1,No2):
        Ans = No1 + No2
        return Ans

    def Subtraction(No1,No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithmatic()

print("Enter 1st num : ")
no1 = int(input())

print("Enter 2nd num : ")
no2 = int(input())

#Ret = Addition(Aobj,no1,no2)
Ret = Aobj.Addition(no1,no2) #error
print("Addition is : ",Ret)

Ret = Aobj.Subtraction(no1,no2) #error
print("Subtraction is : ",Ret)