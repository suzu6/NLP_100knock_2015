# """
# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
# """

# word_p = "パトカー"
# word_t = "タクシー"

# result = ""
# for i in range(len(word_p)):
#     result += word_p[i] + word_t[i]
# print(result)


# word_p = "パトカー"
# word_t = "タクシー"

# result = ""
# for p, t in zip(word_p, word_t):
#     result += p + t
# print(result)

# word_h = "ヘリコプター"
# word_p = "パトカー"

# result = ""
# for h, p in zip(word_h, word_p):
#     result += h + p
# print(result)

# print(list(zip(word_p, word_t)))


# print("".join([''.join(pair) for pair in zip(word_p, word_t)]))

# print("".join(map(lambda x: ''.join(x), zip(word_p, word_t))))

# from functools import reduce 

# word_p = "パトカー"
# word_t = "タクシー"

# print("".join(reduce(lambda p, t: p + t, zip(word_p, word_t))))

# import itertools
# from itertools import chain

# print("".join(itertools.chain(word_p, word_t)))

# print("".join(map(lambda x: "".join(chain(x)), zip(word_p, word_t))))

# import itertools

# word_h = "ヘリコプター"
# word_p = "パトカー"

# result = ""
# for h, p in itertools.zip_longest(word_h, word_p, fillvalue='_'):
#     result += h + p
# print(result)

# import numpy as np

# word_p = "パトカー"
# word_t = "タクシー"

# print(list(map(ord, word_p)))
# arr = np.asarray([list(map(ord, word_p)), list(map(ord, word_t))])
# print(arr.T)
# print(arr.T.tolist())
# result = ''
# for p, t in tuple(arr.T.tolist()):
#     result += chr(p) + chr(t)
    
# print(result)

# import numpy as np

# word_p = "パトカー"
# word_t = "タクシー"


# def zip_by_numpy(str1, str2):
#     arr = np.asarray([list(map(ord, str1)), list(map(ord, str2))])
#     return [(chr(s1), chr(s2)) for s1, s2 in arr.T.tolist()]


# result = ''
# for p, t in zip_by_numpy(word_p, word_t):
#     result += p + t
    
# print(result)


# import numpy as np

# word_p = "パトカー"
# word_t = "タクシー"


# def str_to_int_array(string):
#     return tuple(map(ord, string))


# def int_to_str_array(string):
#     return tuple(map(chr, string))


# def zip_by_numpy(*args):
#     arr = np.asarray(list(map(str_to_int_array, args)))
#     print(arr.T.tolist())
#     return tuple(map(int_to_str_array, arr.T.tolist()))


# result = ''
# for x in zip_by_numpy(word_p, word_t, word_p, word_t):
#     result += ''.join(x)

# print(result)

import numpy as np

word_p = "パトカー"
word_t = "タクシー"


def str_to_int_array(string):
    return list(map(ord, string))


def alternately(*args):
    arr = np.asarray(list(map(str_to_int_array, args)))
    print(arr.tolist())
    print(arr.T.tolist())
    print(arr.T.flatten().tolist())
    return "".join(tuple(map(chr, arr.T.flatten().tolist())))

print(alternately(word_p, word_t + word_p, word_t))
