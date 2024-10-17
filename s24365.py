import os

import pandas as pd
import logging
import requests
from sklearn.preprocessing import StandardScaler

SPREADSHEET_ID = "1vxepXbTeanZrDkztEwUykvAVMPF2lpSh8ZChKJGMOMI"
RANGE = 'Arkusz1!A1:G1001'
API_KEY = os.environ.get('API_KEY')

def get_data():
    logging.info("Odczytywanie danych z arkusza")

    request = requests.get(f'https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{RANGE}?key={API_KEY}')
    data = request.json().get('values', [])

    logging.info('Odczytano dane z arkusza')
    return pd.DataFrame(data[1:], columns=data[0])

def clean_data(dataframe):
    logging.info('Czyszczenie danych')

    # Usuwanie danych
    logging.info('Usuwanie pustych danych')
    dataframe = dataframe.replace("", pd.NA)

    # Konwersja typow danych
    logging.info('Zamiana liczb zapisanych jako tekst na numery')
    dataframe['Wiek'] = pd.to_numeric(dataframe['Wiek'], errors='coerce')
    dataframe['Średnie Zarobki'] = pd.to_numeric(dataframe['Średnie Zarobki'], errors='coerce')

    # Usuwanie wybrakowanych wierszy
    rows_removed = 0
    logging.info('Usuwanie wierszy z <5 uzupełnionymi kolumnami')
    rows_before_removing = len(dataframe)
    dataframe = dataframe.dropna(thresh=5)
    rows_removed += rows_before_removing - len(dataframe)

    # Usuwanie wierszy z brakujacym koncem lub poczatkiem podrozy
    logging.info('Usuwanie wierszy z brakującym czasem początkowym lub końcowym podróży')
    rows_before_removing_trip_times = len(dataframe)
    dataframe = dataframe.dropna(subset=['Czas Początkowy Podróży', 'Czas Końcowy Podróży'])
    rows_removed += rows_before_removing_trip_times - len(dataframe)
    logging.info(f'Usunięto {rows_removed} z {rows_before_removing} wierszy')

    # Uzupelnianie brakujacych wartosci srednimi
    logging.info('Uzupełnianie wierszy z brakującymi danymi')
    rows_modified = 0

    rows_modified += dataframe['Wiek'].isna().sum()
    dataframe.loc[dataframe['Wiek'].isna(), 'Wiek'] = dataframe['Wiek'].mean()

    rows_modified += dataframe['Średnie Zarobki'].isna().sum()
    dataframe.loc[dataframe['Średnie Zarobki'].isna(), 'Średnie Zarobki'] = dataframe['Średnie Zarobki'].mean()
    logging.info(f'Zmodyfikowano {rows_modified} wierszy')

    logging.info('Wyczyszczono dane')
    return dataframe, rows_removed, rows_modified, rows_before_removing

def standardize_data(dataframe):
    logging.info('Standaryzacja danych')

    standard_scaler = StandardScaler()
    dataframe.loc[:, ['Wiek', 'Średnie Zarobki']] = standard_scaler.fit_transform(dataframe[['Wiek', 'Średnie Zarobki']])
    rows_standardized = len(dataframe)

    logging.info('Dane ustandaryzowane')
    return dataframe, rows_standardized

def main():
    dataframe = get_data()
    dataframe_cleaned, rows_removed, rows_modified, rows_before_removing = clean_data(dataframe)
    dataframe_standardized, rows_standardized = standardize_data(dataframe_cleaned)

    with open('report.txt', 'w', encoding='utf-8') as f:
        f.write(f"Usunięto {rows_removed} z {rows_before_removing} wierszy.\n"
                f"Zmodyfikowano {rows_modified} wierszy.\n"
                f"Ustandaryzowano {rows_standardized} wierszy.\n")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        handlers=[logging.FileHandler("log.txt", encoding='utf-8'), logging.StreamHandler()],
                        encoding='utf-8')
    main()