"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

x_str = "paraparaparadise"
y_str = "paragraph"


def n_gram(sentence, N):
    """
    文字のn-gramを返す。
    """
    result = []
    for it in range(len(sentence)):
        if it + N > len(sentence):
            return result
        result.append(sentence[it: it+N])

X = set(n_gram(x_str, N=2))
Y = set(n_gram(y_str, N=2))

print(X)
# => {'is', 'se', 'ad', 'di', 'ap', 'ar', 'pa', 'ra'}
print(Y)
# => {'ph', 'gr', 'ra', 'ap', 'ar', 'pa', 'ag'}

# 和集合　X U Y
_sum = X | Y

print(_sum)
# => {'ar', 'ad', 'is', 'ag', 'pa', 'ap', 'ph', 'ra', 'gr', 'di', 'se'}

_sum = X.union(Y)

print(_sum)
# => {'ar', 'ad', 'is', 'ag', 'pa', 'ap', 'ph', 'ra', 'gr', 'di', 'se'}

# 積集合
_intersection = X & Y

print(_intersection)
# => {'ra', 'ap', 'pa', 'ar'}

# 差集合
_diff_X = X - Y
_diff_Y = Y - X

print(_diff_X)
# => {'is', 'se', 'di', 'ad'}
print(_diff_Y)
# => {'ag', 'gr', 'ph'}

# `se`を含むか

print('se' in X)
# => True

print('se' in Y)
# => False

# 部分集合

print({'se', 'ap'} <= X)
# => True

print({'se', 'ap'} <= Y)
# => False

print(X < X)