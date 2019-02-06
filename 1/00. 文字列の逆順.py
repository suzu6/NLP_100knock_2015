# coding: utf-8

"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

# 回答１
word = "stressed"
rev_word = "".join(reversed(list(word)))
print(word, rev_word)

print()
word = "stressed"

arr = list(word) # ['s', 't', 'r', 'e', 's', 's', 'e', 'd']
print(arr)
arr = reversed(arr) # 
print(str(arr))
print("".join(arr))

# 回答２
word = "1234567890"
rev_word = word[::1]
print(word, rev_word)

rev_word = word[::2]
print(word, rev_word)

rev_word = word[::3]
print(word, rev_word)

# 回答３

word = "stressed"
rev_word = "".join(sorted(word,reverse=True))
print(rev_word)