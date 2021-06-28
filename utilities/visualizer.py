import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint


def test_visualize():
    x = ['А', 'Б', 'В']
    y = [10, 50, 30]

    sns.barplot(x=x, y=y)
    plt.show()


def analyze_data(list_base_image):
    dict_base = {}
    for base_image in list_base_image:
        dict_base[base_image] = 0
        for base_image_checker in list_base_image:
            if base_image == base_image_checker:
                dict_base[base_image] += 1
    return dict_base


def create_data_lists(list_base_image):
    dict_base = analyze_data(list_base_image)
    x = []
    y = []
    for key, value in dict_base.items():
        print(key)
        print(value)
        x.append(key)
        y.append(value)

    return x, y


def visualize_base_images(list_base_image):
    x, y = create_data_lists(list_base_image)
    sns.barplot(x=x, y=y)
    plt.show()


def create_base_image_table(list_base_image):
    x, y = create_data_lists(list_base_image)
    table = pd.DataFrame({'Dockerimage': x, 'Count': y})
    table.to_csv('base_images.csv', index=False)
    data = pd.read_csv("base_images.csv")
    pprint(data)
