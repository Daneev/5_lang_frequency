import itertools
import os
import re
import sys


def load_data(filepath):

    if not os.path.exists(filepath):
        print("There is no file in the specified path.")
        return None

    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def removing_punctuation(text):
    list_clr_word = [re.sub(r'[^\w\s]+', '', s) for s in text.split()]
    return list_clr_word


def create_dict_freq_word(list_clr_word):
    dict_freq_word = {i: list_clr_word.count(i) for i in list_clr_word}
    dict_freq_word.pop('')
    return dict_freq_word


def get_most_frequent_words(text):
    dict_word_result = create_dict_freq_word(removing_punctuation(text))
    ten_frequent_words = (itertools.islice(
        [(dict_word_result[w], w) for w in sorted(dict_word_result, key=dict_word_result.get, reverse=True)], 10))
    return ten_frequent_words


def print_words(words):
    for x, y in list(words): print(x, y)
    return None

def get_path_data():
    if len(sys.argv) > 1:
        return sys.argv[1]  # возвращаем путь к файлу, если программу запустили с параметрами

    print("Введите путь до файла:")
    return input()  # если программа запущена без параметров,
    # ожидаем ввода пути к файлу с клавиатуры.


if __name__ == '__main__':
    print_words(get_most_frequent_words(load_data(get_path_data())))
