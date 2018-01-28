import argparse
import itertools
import re


def get_file():
    parser = argparse.ArgumentParser()

    # required argument
    parser.add_argument('file', help='Enter the path to the text file', type=argparse.FileType('r', encoding='utf-8'))
    with parser.parse_args().file as file:
        return file.read()


def removing_punctuation_from(text):
    list_clr_word = [re.sub(r'[^\w\s]+|[\d]+|[_]+', r'', s) for s in text.split()]
    return list_clr_word


def create_dict_freq_word(list_clr_word):
    dict_freq_word = {i: list_clr_word.count(i) for i in list_clr_word}
    return dict_freq_word


def get_most_frequent_words(text, set_words_count=10):
    dict_word_result = create_dict_freq_word(removing_punctuation_from(text))
    ten_frequent_words = (itertools.islice(
        [(dict_word_result[w], w) for w in sorted(dict_word_result, key=dict_word_result.get, reverse=True) if w != ''],
        set_words_count))
    return ten_frequent_words


def print_result_words(words):
    for x, y in list(words): print(x, y)


if __name__ == '__main__':
    set_words_count = 10
    print_result_words(get_most_frequent_words(get_file(), set_words_count))
