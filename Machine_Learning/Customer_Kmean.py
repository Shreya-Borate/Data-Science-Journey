##################################################################
#
#
###################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans



def main():

    #step 1 : Load the data
    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded with values")
    print(df.head())

    print("Missing Values : ")
    print(df.isnull().sum())


    #step 2 : Feature Selection
    X = df[["AnnualIncome","SpendingScore"]]

    print("Selected Features  : ")
    print(X.head())


    #step 3 : Scale the Data
    scaler = StandardScaler()

    X_Scaled = scaler.fit_transform(X)

    print("Scaled Data : ")
    print(X_Scaled[:5])


    #step 4 : Elbow Method
    WCSS = []
    for k in range (1,11):
        model = KMeans(
            n_clusters= k,
            random_state=42,
            n_init=10
        )

        model.fit(X_Scaled)

        WCSS.append(model.inertia_)

    print("Values of WCSS : ")
    for i in range (len(WCSS)):
        print(f"{i+1} : {WCSS[i]}")


    #step 5 : Visulization
    plt.plot(range(1,11),WCSS, marker = "o")
    plt.xlabel("No.  of clusters")
    plt.ylabel("WCSS")
    plt.title("Marvellous Elbow Method")
    plt.grid(True)
    plt.show()


    #step 6 : Final Model
    model = KMeans(
                    n_clusters= 4,
                    random_state=42,
                    n_init=10
                )
    

    clusters = model.fit_predict(X_Scaled)

    df["Cluster"] = clusters
    print("Dataset with clusters : ")
    print(df.head(100))

if __name__ =="__main__":
    main()