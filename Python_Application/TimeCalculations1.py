def factorial(No):
    fact = 1

    for i in range (1,No+1):
        fact = fact * i
    return fact

def main():
    n= int(input("Enter the number : "))

    Ret = factorial(n)

    print(f"Factorial of {n} is : {Ret}")

if __name__ == "__main__":
    main()