import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df = pd.read_csv("nodar_melkonyan_1_81429765.csv")

X = df[['words', 'links', 'capital_words', 'spam_word_count']]
y = df['is_spam']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

coefficients = pd.Series(model.coef_[0], index=X.columns)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Not Spam", "Spam"])
disp.plot(cmap="Blues")
plt.title("Confusion Matrix")

#.pkl ფაილად გადაკეთება
with open("spam_model.pkl", "wb") as file:
    pickle.dump(model, file)
