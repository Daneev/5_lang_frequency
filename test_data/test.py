from lang_frequency import get_most_frequent_words


def test_text():
    text = 'vkjds fgvbkjdsbv kljfsglvl v675rt 73487 AAA   42638gdfguye rtf7 ew  ' \
           'ew fdj nvkfdnvk-- +_(_*^$ ew $@# KLJNKJH KJF^GV htfhsa fdfdfygyрпоы ' \
           'впоавып аыгвпалгдывапвыра шщ гн48 78н6 8нщ4ге 5щшорлшоаш  вашпржав ' \
           'рпщжшвна пщжавнщ жв щ9ваываfvxfcvкек 8щ7е5г _ _ _ _ _'

    gf = get_most_frequent_words(text)
    test_list = list(gf)

    assert test_list == [(3, 'ew'),
                         (1, 'vkjds'),
                         (1, 'fgvbkjdsbv'),
                         (1, 'kljfsglvl'),
                         (1, 'vrt'),
                         (1, 'AAA'),
                         (1, 'gdfguye'),
                         (1, 'rtf'),
                         (1, 'fdj'),
                         (1, 'nvkfdnvk')
                         ]
