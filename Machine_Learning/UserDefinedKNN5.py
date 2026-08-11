import math
import numpy as np

def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2   +  (P1['Y'] - P2['Y'])**2)
    return Ans

def MarvellousKNNClassifier():
    border = "-"*60

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

    new_point = {'X' : 3, 'Y' : 3}

    print("Distances of All points : ")
    print(border)
    for d in Data:
        d['distance'] = MarvellousEucDistance(d,new_point)

    for d in Data:
        print(d['distance'],d['Label'])

    print(border)

def main():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()