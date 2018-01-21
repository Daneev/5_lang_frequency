import itertools
import os, re

def load_data(filepath):

    if not os.path.exists(filepath):
        print("There is no file in the specified path.")
        return None

    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def get_most_frequent_words(text):
    list_word = [re.sub(r'[^\w\s]+', '', s) for s in text.split()]
    result = {i: list_word.count(i) for i in list_word}
    result.pop('')
    #print(list_word)
    #print(result)
    #print(list(result.keys())[list(result.values()).index(54)])
    #result1 = sorted(result.items(), key=lambda x: x[1], reverse=True)
    #print(result1[:10])
    #print(sorted((value, key) for (key, value) in result.items(), reverse=True))
    #print(sorted(result, key=result.get, reverse=True))
    #for w in sorted(result, key=result.get, reverse=True):
        #print(result[w], w)

    world = (itertools.islice([(result[w], w) for w in sorted(result, key=result.get, reverse=True)], 10))
    for x, y in list(world): print(x, y)


if __name__ == '__main__':
    print(get_most_frequent_words(load_data('data_for_test/text.txt')))


