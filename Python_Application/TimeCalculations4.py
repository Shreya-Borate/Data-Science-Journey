import time
def factorial(No):
    fact = 1

    for i in range (1,No+1):
        fact = fact * i
    return fact

def main():
    n= int(input("Enter the number : "))

    start_time = time.time()

    Ret = factorial(n)

    end_time = time.time()

    print(f"Factorial of {n} is : {Ret}")

    print(f"Time required is : {end_time - start_time:.5f} seconds")

    

if __name__ == "__main__":
    main()