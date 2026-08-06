from MarvellousLibrary import filterX, mapX, reduceX

CheckEven = lambda No : (No%2 == 0)

increment = lambda No : No+1

Addition = lambda No1, No2 : No1 + No2


def main ():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filterX(CheckEven,Data))   # this fun should only return boolean and should have 1 parameter

    print("data after filter : ",FData)

    MData = list(mapX(increment,FData))

    print("Data After  map : ",MData)

    RData = reduceX(Addition,MData)

    print("Data after Reduce : ",RData)

if __name__ =="__main__":
    main()