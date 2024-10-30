# Eksploracja i analiza danych

Zbiór danych zawiera informacje na temat wpływu różnych czynników na wyniki w testach przeprowadzanych wśród uczniów
ostatniej klasy w szkołach średnich.
Zbiór zawiera następujące czynniki:

- **gender**: Płeć badanej osoby.
- **ethnicity**: Pochodzenie etniczne (Afroamerykanin, Latynos etc.).
- **score**: Wynik testu osiągnięć. Testy te są pisane przez uczniów ostatniej klasy szkół wyższych.
- **fcollege**: Czy ojciec jest absolwentem uczelni wyższej?
- **mcollege**: Czy matka jest absolwentką uczelni wyższej?
- **home**: Czy rodzina posiada dom na własność?
- **urban**: Czy szkoła znajduje się w obszarze miejskim?
- **unemp**: Stopa bezrobocia w powiecie w roku 1980.
- **wage**: Stawka godzinowa w przemyśle w danym stanie w roku 1980.
- **distance**: Odległość od uczelni (w 10 milach).
- **tuition**: Średnie czesne na uczelni (w 1000 USD).
- **education**: Lata edukacji.
- **income**: Czy dochód rodziny przekracza 25,000 USD rocznie?
- **region**: Region (Zachód etc.).

W podfolderze **charts** umieszczone zostały wykresy pokazujące dane z datasetu.

## Inżynieria cech i przygotowanie danych

Do wyczyszczenia danych pod trenowanie modelu wykonałam następujące kroki:

1. Dane nie miały żadnych pustych pól, więc pominęłam usuwanie wybrakowanych wierszy.
2. Usunęłam kolumnę opisującą numer wiersza. Kolejność danych nie ma znaczenia, więc zakłamywałoby to wynik.
3. Dane liczbowe przekonwertowałam na zmienną numeryczną.
4. Dane opisowe zostały zakodowane jako numery, abym mogła użyć modelu regresji liniowej.
5. Dane zostały ustandaryzowane.

# Wybór i trenowanie modelu

Do wykonania zadania użyłam modelu regresji liniowej wielorakiej.
Regresja liniowa jest odpowiednim modelem do przewidywania wartości ciągłych - a taką wartością jest zmienna **score**.
Zbiór danych zawierał dużo zmiennych liczbowych i binarnych, przez co konwersja danych na liczbowe była
prosta w wykonaniu.

# Ocena modelu

Mój model osiągnął następujące wyniki:
- **MSE**: 49.11379769495445
- **MAE**: 5.754310603829265
- **RMSE**: 7.008123692897725
- **R2**: 0.35233729278740866

Oznacza to, że model nie jest najbardziej dokładny i popełnia spore błędy przy przewidywaniu zmiennej score.
