"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

$ python 14.\ 先頭からN行を出力.py 5 hightemp.txt
高知県  江川崎  41      2013-08-12
埼玉県  熊谷    40.9    2007-08-16
岐阜県  多治見  40.9    2007-08-16
山形県  山形    40.8    1933-07-25
山梨県  甲府    40.7    2013-08-10
和歌山県        かつらぎ        40.6    1994-08-08

"""
import sys


def readlines_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

N, file_name = sys.argv[1:3]


lines = readlines_file(file_name)

print("".join(lines[:int(N)+1]))