"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

import re


def cipher(src):
    """
    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    """
    return re.sub(r'[a-z]', lambda c: chr(219 - ord(c.group(0))), src)

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 暗号化
print(cipher(text))
# => Hr Hv Lrvw Bvxzfhv Blilm Clfow Nlg Ocrwrav Foflirmv. Nvd Nzgrlmh Mrtsg Aohl Srtm Pvzxv Svxfirgb Cozfhv. Aigsfi Krmt Czm.

# 復号化
print(cipher(cipher(text)))
# => Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.


def dashrepl(matchobj):
    if matchobj.group(0) == '-':
        return ' '
    else:
        return '-'

print(re.sub('-{1,2}', dashrepl, 'pro----gram-files'))

print('a+z', ord('a') + ord('z'))
print('A+Z', ord('A') + ord('Z'))


def cipher(src):
    """
    英小文字ならば(219 - 文字コード)の文字に置換
    英大文字ならば(155 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    """
    tmp = re.sub(r'[a-z]', lambda m: chr(219 - ord(m.group(0))), src)
    return re.sub(r'[A-Z]', lambda m: chr(155 - ord(m.group(0))), tmp)

# 暗号化
print(cipher(text))
# => Sr Sv Orvw Yvxzfhv Ylilm Xlfow Mlg Lcrwrav Uoflirmv. Mvd Mzgrlmh Nrtsg Zohl Hrtm Kvzxv Hvxfirgb Xozfhv. Zigsfi Prmt Xzm.

# 復号化
print(cipher(cipher(text))) 
# => Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.
