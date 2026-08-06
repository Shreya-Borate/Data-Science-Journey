

#2+4+6+8 = 20
def SumEven(No):
    sum = 0
    for i in range (2,No,2):
        sum += i

    print("Summation of even : ",sum)

#1+3+5+7+9 = 25
def SumOdd(No):
    sum = 0
    for i in range (1,No,2):
        sum += i

    print("Summation of odd : ",sum)

def main():
    SumEven(100000)
    SumOdd(100000)
    

if __name__ == "__main__":
    main()