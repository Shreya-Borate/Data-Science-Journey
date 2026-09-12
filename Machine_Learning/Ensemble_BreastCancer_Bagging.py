import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#----------------------------------
# Step 1 : Load the Dataset
#----------------------------------

df = pd.read_csv("breast_cancer.csv")

print("Shape of Dataset : ",df.shape)

print("First few records : ")
print(df.head())

#--------------------------------------------------
# Step 2 : Separate Features and labels
#--------------------------------------------------

X = df.drop("target", axis=1)
Y = df["target"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)


#--------------------------------------------------
# Step 3 : Split dataset for traning and testing
#--------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


#--------------------------------------------------
# Step 4 : Scale the Features
#--------------------------------------------------

scaler =  StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)


#--------------------------------------------------
# Step 5.1 : Create the Base Model
#--------------------------------------------------

base_model =DecisionTreeClassifier(random_state=42)


#--------------------------------------------------
# Step 5.2 : Create the Bagging Model
#--------------------------------------------------

model = BaggingClassifier(
    estimator=base_model,
    n_estimators=10,
    random_state=42
)

#--------------------------------------------------
# Step 6 : Train The Model
#--------------------------------------------------

model = model.fit(X_train, Y_train)


#--------------------------------------------------
# Step 7 : Test the Model
#--------------------------------------------------

y_pred = model.predict(X_test)


#--------------------------------------------------
# Step 8 : Evaluate the Model
#--------------------------------------------------

print("Accuracy : ",accuracy_score(Y_test,y_pred))

print("Confusion matrix : ")
print(confusion_matrix(Y_test,y_pred))




