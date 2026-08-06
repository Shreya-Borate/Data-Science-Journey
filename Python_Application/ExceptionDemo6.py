def main():
    Ans = 0
    try:
        print("Enter first no : ")
        No1 = int(input())

        print("Enter second no : ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is sucessful")

    except ZeroDivisionError as zobj:
        print("Exception Occured due to 2nd operant is zero : ",zobj)

    except ValueError as vobj:
        print("Exception occured due to invalid datatype : ",vobj)

    except Exception as eobj:
        print("Exception occured : ",eobj)

    finally:
        print("Inside Finally block")

    print("Result is : ",Ans)

if __name__ == "__main__":
    main()