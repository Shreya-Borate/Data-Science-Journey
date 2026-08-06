def CheckEven(No):
    return (No % 2 == 0)

def main():
    value = int(input("Enter Number : "))

    Ret = CheckEven(value)

    if (Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd Number")

if __name__ == "__main__":
    main()