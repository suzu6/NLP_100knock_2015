"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

import re

sentence = "I am an NLPer"


def word_n_gram(sentence, N):
    """
    単語のn-gramを返す。
    """
    words = sentence.split()
    result = []
    for it, c in enumerate(words):
        if it + N > len(words):
            return result
        result.append(words[it: it+N])


def char_n_gram(sentence, N):
    """
    文字のn-gramを返す。
    """
    result = []
    for it in range(len(sentence)):
        if it + N > len(sentence):
            return result
        result.append(sentence[it: it+N])

print(word_n_gram(sentence, N=2))
# => [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]

print(word_n_gram(sentence, N=3))
# => [['I', 'am', 'an'], ['am', 'an', 'NLPer']]

print(char_n_gram(sentence, N=2))
# => ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

print(char_n_gram(sentence, N=3))
# => ['I a', ' am', 'am ', 'm a', ' an', 'an ', 'n N', ' NL', 'NLP', 'LPe', 'Per']

print(char_n_gram(sentence.split(), N=3))
# => [['I', 'am', 'an'], ['am', 'an', 'NLPer']]
