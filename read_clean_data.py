import pandas as pd
import logging

from sklearn.preprocessing import StandardScaler

def get_data(file_path):
    logging.info("Odczytywanie danych z pliku")
    return pd.read_csv(file_path)

def clean_data(dataframe):
    logging.info('Czyszczenie danych')

    # Usuniecie kolumny rowname
    logging.info('Usuwanie kolumny rownames')
    dataframe.drop(columns=['rownames'], inplace=True)

    # Konwersja typow danych
    logging.info('Zamiana liczb zapisanych jako tekst na numery')
    dataframe['score'] = pd.to_numeric(dataframe['score'], errors='coerce')
    dataframe['unemp'] = pd.to_numeric(dataframe['unemp'], errors='coerce')
    dataframe['wage'] = pd.to_numeric(dataframe['wage'], errors='coerce')
    dataframe['distance'] = pd.to_numeric(dataframe['distance'], errors='coerce')
    dataframe['tuition'] = pd.to_numeric(dataframe['tuition'], errors='coerce')
    dataframe['education'] = pd.to_numeric(dataframe['education'], errors='coerce')
    dataframe[['score', 'unemp', 'wage', 'distance', 'tuition', 'education']] = \
        dataframe[['score', 'unemp', 'wage', 'distance', 'tuition', 'education']].astype(float)

    return dataframe

def text_conversion(dataframe):
    dataframe = pd.get_dummies(dataframe, drop_first=True)
    return dataframe

def standardize_data(dataframe):
    # Standaryzacja danych
    logging.info('Standaryzacja danych')
    standard_scaler = StandardScaler()
    dataframe.loc[:, ['score', 'unemp', 'wage', 'distance', 'tuition', 'education']] = (
        standard_scaler.fit_transform(dataframe[['score', 'unemp', 'wage', 'distance', 'tuition', 'education']].astype(float)))
    rows_standardized = len(dataframe)
    logging.info('Dane ustandaryzowane. Ustandaryzowano %s wierszy', rows_standardized)

    logging.info('Wyczyszczono dane')
    return dataframe

def prepare_data(file_path):
    dataframe = get_data(file_path)
    dataframe = clean_data(dataframe)
    dataframe = text_conversion(dataframe)

    return dataframe

def main(file_path):
    dataframe = prepare_data(file_path)
    print(dataframe)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        encoding='utf-8')
    main("./CollegeDistance.csv")
