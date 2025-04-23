import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("nodar_melkonyan_1_81429765.csv")

X = df[['words', 'links', 'capital_words', 'spam_word_count']]
y = df['is_spam']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

coefficients = pd.Series(model.coef_[0], index=X.columns)

print(coefficients)