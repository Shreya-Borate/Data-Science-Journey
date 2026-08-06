def CheckEven(No):
    if (No % 2 == 0):
        print("Its is Even Number")
    else:
        print("Its is Odd Number")

def main():
    value = int(input("Enter Number : "))

    CheckEven(value)

if __name__ == "__main__":
    main()