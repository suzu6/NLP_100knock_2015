"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""


def readlines_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()


def save_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)


cal1 = readlines_file('cal1.txt')
cal2 = readlines_file('cal2.txt')

# 改行や空白文字を削除
cal1 = list(map(lambda x: x.strip(), cal1))
cal2 = list(map(lambda x: x.strip(), cal2))

# タブ区切りで並べたリストを作成
lines = ["{0}\t{1}".format(line1, line2) for line1, line2 in zip(cal1, cal2)]

save_file('marge.txt', "\n".join(lines))
