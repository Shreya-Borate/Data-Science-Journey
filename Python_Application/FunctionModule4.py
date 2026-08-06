from Marvellous import Addition, substraction

def main():
    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    Ret = Addition(value1, value2)  

    print("Addition is : ",Ret)

    Ret = substraction(value1, value2) #Error

    print("Substraction is : ",Ret)

if __name__ == "__main__":
    main()