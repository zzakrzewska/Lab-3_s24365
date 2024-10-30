import logging
import os

import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
import seaborn as sns

from read_clean_data import get_data, clean_data

def generate_histplot(dataframe, column):
    plot.figure()
    sns.histplot(dataframe[column], kde=True)
    plot.title(f'{column}')
    plot.xlabel(column)
    plot.ylabel('Ilość')
    plot.savefig(os.path.join('./charts', f'rozklad_{column}.png'))
    plot.close()

def generate_countplot(dataframe, column):
    plot.figure()
    sns.countplot(dataframe[column])
    plot.title(f'{column}')
    plot.xlabel(column)
    plot.ylabel('Ilość')
    plot.savefig(os.path.join('./charts', f'{column}_chart.png'))
    plot.close()

def generate_countplot_bool(dataframe, column):
    plot.figure()
    sns.countplot(dataframe[column])
    plot.title(f'{column}')
    plot.xlabel(column)
    plot.ylabel('Ilość')
    plt.xticks(ticks=[0,1])
    plot.savefig(os.path.join('./charts', f'{column}_chart.png'))
    plot.close()

def generate_plots(dataframe):
    if not os.path.exists('./charts'):
        os.makedirs('./charts')

    # Generowanie wykresów dla kolumn numerycznych
    logging.info('Generowanie wykresów dla kolumn numerycznych')
    num_columns = dataframe.select_dtypes(include=[float]).columns.tolist()
    for column in num_columns:
        generate_histplot(dataframe, column)

    # Generowanie wykresów dla kolumn tekstowych
    logging.info('Generowanie wykresów dla kolumn tekstowych')
    text_columns = dataframe.select_dtypes(include=[object]).columns.tolist()
    for column in text_columns:
        generate_countplot(dataframe, column)


def main(file_path):
    dataframe = clean_data(get_data(file_path))
    generate_plots(dataframe)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        encoding='utf-8')
    main("./CollegeDistance.csv")
