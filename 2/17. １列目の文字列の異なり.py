"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

lines = read_file('hightemp.txt').split('\n')

# 空行の削除
lines = list(filter(lambda line: line != '', lines))

# 1列目の取り出し
cal1 = set(map(lambda line: line.split('\t')[0].strip(), lines))

print("\n".join(cal1))

"""
山梨県
静岡県
岐阜県
和歌山県
愛媛県
群馬県
愛知県
千葉県
高知県
埼玉県
山形県
大阪府
"""