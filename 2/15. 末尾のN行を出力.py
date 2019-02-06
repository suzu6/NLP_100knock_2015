"""
15. 末尾のN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

$ python 15.\ 末尾のN行を出力.py 2 hightemp.txt
山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02

$ python 15.\ 末尾のN行を出力.py 5 hightemp.txt
埼玉県  鳩山    39.9    1997-07-05
大阪府  豊中    39.9    1994-08-08
山梨県  大月    39.9    1990-07-19
山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02

"""

import sys


def readlines_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

N, file_name = sys.argv[1:3]


lines = readlines_file(file_name)

print("".join(lines[-1 * int(N):]))