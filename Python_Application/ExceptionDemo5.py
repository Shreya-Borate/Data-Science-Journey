def main():
    Ans = 0
    try:
        print("Enter first no : ")
        No1 = int(input())

        print("Enter second no : ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is sucessful")

    except Exception as eobj:
        print("Exception occured : ",eobj)




    print("Result is : ",Ans)

if __name__ == "__main__":
    main()