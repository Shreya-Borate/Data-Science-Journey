def MarvellousKNNClassifier():
    border = "-"*40

    Data = [
        {'point' : 'A', 'X' : 1, 'Y' : 2, 'Label' : 'Red'},
        {'point' : 'B', 'X' : 2, 'Y' : 3, 'Label' : 'Red'},
        {'point' : 'C', 'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
        {'point' : 'D', 'X' : 5, 'Y' : 6, 'Label' : 'Blue'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for i in Data:
        print(i)

    print(border)

def main():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()