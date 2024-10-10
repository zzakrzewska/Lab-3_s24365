# s24365.py
import numpy as np
from random import randint
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generowanie prostego zbioru danych
def generate_data():
    np.set_printoptions(precision=5, suppress=True)

    set0_count = randint(50, 100)
    set1_count = randint(50, 100)

    set0 = np.random.randn(set0_count, 2)
    set1 = np.random.randn(set1_count, 2) + np.array([2, 2])

    label0 = np.zeros(set0_count)
    label1 = np.ones(set1_count)

    x = np.vstack((set0, set1))
    y = np.hstack((label0, label1))

    return x, y

# Trenowanie prostego modelu regresji logistycznej
def train_model():
    x, y = generate_data()

    # Podział na zbiór treningowy i testowy
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # Trenowanie modelu
    model = LogisticRegression()
    model.fit(x_train, y_train)
    
    # Predykcja na zbiorze testowym
    prediction = model.predict(x_test)
    
    # Wyliczenie dokładności
    accuracy = accuracy_score(y_test, prediction)

    # Zapis wyniku
    with open('accuracy.txt', 'w') as file:
        file.write(f"Model trained with accuracy: {accuracy * 100:.2f}%\n")

if __name__ == "__main__":
    train_model()
