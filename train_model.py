import logging

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split

from read_clean_data import prepare_data

def split_data(dataframe):
    logging.info('Podział danych na testowe i treningowe')
    x = dataframe.drop('score', axis=1)
    y = dataframe['score']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    return x_train, x_test, y_train, y_test

def train_model(x_train, x_test, y_train, y_test):
    model = LinearRegression()

    # Trenowanie modelu
    logging.info('Trenowanie modelu')
    model.fit(x_train, y_train)

    logging.info('Predykcja')
    predictions = model.predict(x_test)

    logging.info('Ocena modelu')
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = root_mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    logging.info(f'MSE: {mse}')
    logging.info(f'MAE: {mae}')
    logging.info(f'RMSE: {rmse}')
    logging.info(f'R2: {r2}')

def main(file_path):
    dataframe = prepare_data(file_path)
    x_train, x_test, y_train, y_test = split_data(dataframe)
    train_model(x_train, x_test, y_train, y_test)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        encoding='utf-8')
    main("./CollegeDistance.csv")
