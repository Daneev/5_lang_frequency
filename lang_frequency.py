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
    """ To count the same words, you need to bring the text to the same register and clear of the punctuation """

    text_lower = text.lower()
    return [re.sub(r'[^\w\s]+|[\d]+|[_]+', r'', s) for s in text_lower.split()]


def create_dict_freq_word(list_clr_word):
    return {word: list_clr_word.count(word) for word in list_clr_word}


def get_most_frequent_words(text, set_words_count=10):
    dict_freq_word = create_dict_freq_word(removing_punctuation_from(text))
    return list(itertools.islice(
        [(dict_freq_word[w], w) for w in sorted(dict_freq_word, key=dict_freq_word.get, reverse=True) if w != ''],
        set_words_count))


def print_result_words(words):
    for x, y in words: print(x, y)


if __name__ == '__main__':
    set_words_count = 10
    print_result_words(get_most_frequent_words(get_file(), set_words_count))
