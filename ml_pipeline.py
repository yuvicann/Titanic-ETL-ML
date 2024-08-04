import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from data_loading import load_data_from_db

def train_ml_model(data):
    X = data.drop(columns=['Survived'])
    y = data['Survived']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000, penalty='l2')
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

if __name__ == "__main__":
    data = load_data_from_db()
    accuracy = train_ml_model(data)
    print(f"Model Accuracy: {accuracy:.2f}")
