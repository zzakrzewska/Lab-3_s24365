# Lab4 - analizator wyników
Aplikacja przewiduje wynik score studenta na podstawie danych wejściowych. Model wytrenowany jest na pliku _CollegeDistance.csv_

## Klonowanie repozytorium
W celu sklonowania repozytorium potrzebny jest zainstalowany **git**.
Po zainstalowaniu należy sklonować repozytorium poprzez wpisanie następujących komend w terminal:
    
    git clone https://github.com/zzakrzewska/Lab-4_s24365.git
    cd Lab-4_s24365

## Uruchomienie aplikacji lokalnie
W celu uruchomienia aplikacji potrzebny jest zainstalowany **python 3.12**.
Po zainstalowaniu należy:
1. Zainstalować wymagane zależności:
   
        pip install -r requirements.txt

2. Wytrenować model:
    
        python train_model.py

3. Uruchomić API:

        python api.py

## Uruchomienie aplikacji z wykorzystaniem _Dockera_
W celu uruchomienia aplikacji poprzez docker potrzebny jest zainstalowany **docker**.
Po zainstalowaniu należy:
1. Pobrać obraz z docker hub:

        docker pull zosiazak/lab4
2. Uruchomić aplikację:
        
        docker run -p 5000:5000 zosiazak/lab4:latest

Aplikacja będzie działać pod adresem http://127.0.0.1:5000.

## Wysyłanie żądań do API
Aby uzyskać wynik predykcji, niezależnie od tego czy aplikacja została uruchomiona lokalnie czy przez dockera,
potrzebna jest aplikacja do wysyłania żądań HTTP, np. Postman, lub np. odpowiedni skrypt w pythonie.

Aplikacja posiada jeden endpoint: POST /collegeDistance.
Endpoint wymaga wysłania nagłówka:

        'Content-Type': 'application/json'

Oraz body z danymi wejściowymi do wykonania przewidywania.

Przykładowe dane wejściowe:
    
    {
        "unemp": -0.505635,
        "wage": -1.050324,
        "distance": -0.697845,
        "tuition": 0.219584,
        "education": -1.010536,
        "gender_male": true,
        "ethnicity_hispanic": true,
        "ethnicity_other": true,
        "fcollege_yes": true,
        "mcollege_yes": false,
        "home_yes": true,
        "urban_yes": true,
        "income_low": false,
        "region_west": false
    }

Odpowiedź zostanie wysłana jako JSON:

    {
        "prediction": 0.6689511636269718
    }