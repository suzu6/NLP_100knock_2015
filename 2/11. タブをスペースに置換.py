"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

# import re

# with open('hightemp.txt', 'r') as file:
#     text = re.sub(r'\t', ' ', file.read())
#     print(text)

f = open('sample.txt', 'r')

    f.close()

with open('sample.txt', 'r') as f:
    f.read()