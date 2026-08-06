import time
import multiprocessing
import os 


def SumEven(No):
    print(f"PiD of SumEven : {os.getpid()} PPid of SumEven : {os.getppid()}")
    sum = 0
    for i in range (2,No,2):
        sum += i

    print("Summation of even : ",sum)


def SumOdd(No):
    print(f"PiD of SumOdd : {os.getpid()} PPid of SumOdd : {os.getppid()}")
    sum = 0
    for i in range (1,No,2):
        sum += i

    print("Summation of odd : ",sum)

def main():

    print(f"PiD of main : {os.getpid()} PPid of main : {os.getppid()}")

    start_time = time.perf_counter()

    t1 = multiprocessing.Process(target=SumEven(100,))

    t2 = multiprocessing.Process(target=SumOdd(100,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    end_time = time.perf_counter()

    print(f"Time Required : {end_time - start_time:.4f}")
    

if __name__ == "__main__":
    main()