import time
import threading


def SumEven(No):
    print("TID of sumEven thread is : ",threading.get_ident())


def SumOdd(No):
    print("TID of sumOdd thread is : ",threading.get_ident())

def main():

    print("TID of Main thread is : ",threading.get_ident())

    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven(100,))

    t2 = threading.Thread(target=SumOdd(100,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    end_time = time.perf_counter()

    print(f"Time Required : {end_time - start_time:.4f}")
    

if __name__ == "__main__":
    main()