"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def save_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)


lines = read_file('hightemp.txt').split('\n')

# 空行の削除
lines = list(filter(lambda line: line != '', lines))

# 指定列の取り出し
cal1 = list(map(lambda line: line.split('\t')[0], lines))
cal2 = list(map(lambda line: line.split('\t')[1], lines))

save_file('cal1.txt', "\n".join(cal1))
save_file('cal2.txt', "\n".join(cal2))