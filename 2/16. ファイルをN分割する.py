"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import sys


def readlines_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()


def save_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)


def suffix(i):
    # 3桁の０埋め
    return "{:03d}".format(i)


N, file_name, prefix = sys.argv[1:4]


lines = readlines_file(file_name)

# 切り分ける行数
limit = len(lines) // int(N)

for i in range(int(N)):
    offset = i * limit
    # 分割
    text = lines[offset: offset + limit]
    save_file(prefix + suffix(i), "".join(text))