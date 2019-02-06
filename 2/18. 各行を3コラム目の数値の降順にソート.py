"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）
"""


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

lines = read_file('hightemp.txt').split('\n')

# 空行の削除
lines = list(filter(lambda line: line != '', lines))

# 行をタブで分割
lines = list(map(lambda line: line.split('\t'), lines))

# 指定列で逆順ソート
lines = sorted(lines, key=lambda x: x[2], reverse=True)

# タブ区切りで行を結合
lines = list(map(lambda x: "\t".join(x), lines))

print("\n".join(lines))