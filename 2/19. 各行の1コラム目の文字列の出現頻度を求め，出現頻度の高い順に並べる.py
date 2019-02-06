"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""
import collections


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

lines = read_file('hightemp.txt').split('\n')

# 空行の削除
lines = list(filter(lambda line: line != '', lines))

# 行をタブで分割
lines = list(map(lambda line: line.split('\t'), lines))

# 1列目の取り出し
cal1 = list(map(lambda line: line[0].strip(), lines))

# 要素と数を多い順に取り出す。
counted_cal1 = collections.Counter(cal1).most_common()
print(counted_cal1)
# => [('埼玉県', 3), ('山形県', 3), ('山梨県', 3), ('群馬県', 3), ('岐阜県', 2), ('静岡県', 2), ('愛知県', 2), ('千葉県', 2), ('高知県', 1), ('和歌山県', 1), ('愛媛県', 1), ('大阪府', 1)]

# タブ区切りで行を結合
counted_cal1 = list(map(lambda x: f'{x[1]}\t{x[0]}', counted_cal1))

print("\n".join(counted_cal1))
"""
3       埼玉県
3       山形県
3       山梨県
3       群馬県
2       岐阜県
2       静岡県
2       愛知県
2       千葉県
1       高知県
1       和歌山県
1       愛媛県
1       大阪府
"""
