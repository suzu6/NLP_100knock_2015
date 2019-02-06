# coding: utf-8

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""


import gzip
import json
import re


def read_wiki(fname, tiltle):
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']


def is_category(string):
    return re.match(r'^\[\[Category:.+\]\]$', string)


def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname, 'イギリス').split('\n')

    # カテゴリの行を表示する
    for line in text:
        if is_category(line):
            print(line)


if __name__ == '__main__':
    main()

"""
$ python 21.\ カテゴリ名を含む行を抽出.py
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""