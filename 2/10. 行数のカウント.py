"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

f = open('hightemp.txt', 'r')
print('length', len(f.readlines()))

f.close()