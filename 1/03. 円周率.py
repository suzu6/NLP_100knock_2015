"""
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures 
involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）
文字数を先頭から出現順に並べたリストを作成せよ．
"""

import re
import math

sentensce = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

# ,.スペースで分ける
words = re.split(r'[,.]? ?', sentensce)

# 空文字を削除
words = list(filter(lambda w: w != '', words))

print(words)
# => ['Now', 'I', 'need', 'a', 'drink', 'alcoholic', 'of', 'course', 'after', 'the', 'heavy', 'lectures', 'involving', 'quantum', 'mechanics']

words_len = list(map(len, words))

print(words_len)

print(math.pi)