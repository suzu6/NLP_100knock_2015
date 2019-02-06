"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

import re

sentensce = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# 1文字取り出す単語
initials = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# ,.スペースで分ける
words = sentensce.split()


print(words)
# => ['Hi', 'He', 'Lied', 'Because', 'Boron', 'Could', 'Not', 'Oxidize', 'Fluorine', 'New', 'Nations', 'Might', 'Also', 'Sign', 'Peace', 'Security', 'Clause', 'Arthur', 'King', 'Can']

# 元素記号
element_symbols = {}

for it, word in enumerate(words):
    if it + 1 in initials:
        # 先頭一文字だけ
        element_symbols[it+1] = word[0]
    else:
        # ２文字
        element_symbols[it+1] = word[:2]

print(element_symbols)
# => {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mi', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}


char2 = list(map(lambda x: x[:2], words))

element_symbols = {it+1: word[0] if it + 1 in initials else word[:2] for it, word in enumerate(words)}

print(element_symbols)