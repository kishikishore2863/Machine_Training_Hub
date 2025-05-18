from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

emails = [
    "Win money now", "Hello friend, how are you?", "Cheap meds available",
    "Important meeting tomorrow", "Buy cheap watches", "Are you free today?"
]

labels = [1,0,1,0,1,0]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(emails)

X_train, X_test, y_train, y_test = train_test_split(x,labels,test_size=0.33,random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accurancy:", accuracy_score(y_test,y_pred))
print("Predict labels:",y_pred)


