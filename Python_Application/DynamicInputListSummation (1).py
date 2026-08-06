def summation(Data):
    sum = 0

    for no in Data:
        sum+=no
    return sum

def main():
    Size = 0
    Arr = list()

    print("Enter the Number of elements: ")
    Size = int(input())

    print("Enter the elements: ")

    for i in range (Size):
        no = int(input())
        Arr.append(no)
    
    Ret = summation(Arr)

    print(Arr)



if __name__ == "__main__":
    main()