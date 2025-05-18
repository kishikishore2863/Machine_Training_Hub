import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = {
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Scores":[10,20,30,40,50,60,70,80,90,100]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
Y = df["Scores"]

model = LinearRegression()
model.fit(X,Y)

predicted = model.predict([[6]])
print("predicted score for 6hours:",predicted[0])

plt.scatter(X,Y,color="blue")
plt.plot(X,model.predict(X),color = "red")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.title("study Hours vs Score")
plt.show()