import pandas as pd 

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

#---------------------------------------------------------
# step 1 : Load the Data
#---------------------------------------------------------

df = pd.read_csv("california_housing.csv")

print("Shape of Dataset : ",df.shape)
print("First few records : ",df.head())


#---------------------------------------------------------
# step 2 : Separate features and Labels
#---------------------------------------------------------

X = df.drop("target", axis=1)
Y = df["target"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)


#--------------------------------------------------
# Step 3 : Split dataset for traning and testing
#--------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


#--------------------------------------------------
# Step 4 : Create the Model
#--------------------------------------------------

model = DecisionTreeRegressor(random_state=42)


#--------------------------------------------------
# Step 5 : Train The Model
#--------------------------------------------------

model = model.fit(X_train, Y_train)


#--------------------------------------------------
# Step 6 : Test the Model
#--------------------------------------------------

y_pred = model.predict(X_test)


#--------------------------------------------------
# Step 7 : Evaluate the Model
#--------------------------------------------------

print("MSE : ",mean_squared_error(Y_test,y_pred))
print("R2  : ",r2_score(Y_test,y_pred))



