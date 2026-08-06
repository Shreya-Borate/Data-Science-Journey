import time
import threading


def SumEven(No):
    sum = 0
    for i in range (2,No,2):
        sum += i

    print("Summation of even : ",sum)


def SumOdd(No):
    sum = 0
    for i in range (1,No,2):
        sum += i

    print("Summation of odd : ",sum)

def main():

    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven(1000000,))

    t2 = threading.Thread(target=SumOdd(1000000,))

    t1.start()
    t2.start()


    end_time = time.perf_counter()

    print(f"Time Required : {end_time - start_time:.4f}")
    

if __name__ == "__main__":
    main()