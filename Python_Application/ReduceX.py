from functools import reduce

def CheckEven(No):
    return(No%2 == 0)

def increment(No):
    return No+1

def Addition (No1, No2):
    return No1 + No2



def main ():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filter(CheckEven,Data))   # this fun should only return boolean and should have 1 parameter

    MData = list(map(increment,FData))


    print("data after filter : ",FData)

    print("Data After  map : ",MData)

    RData = reduce(Addition,MData)

    print("Data after Reduce : ",RData)

if __name__ =="__main__":
    main()