# coding: utf-8

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ
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


def get_category_name(string):
    m = re.match(r'^\[\[Category:(.*?)(\|.*)?\]\]$', string)
    # m.group(1) => 'category_name'
    return m.group(1)


def get_category_name2(string):
    m = re.match(r'^\[\[Category:(.*)\]\]$', string)
    # m.group(1) => 'category_name' or 'category_name|*'
    return m.group(1).split('|')[0]


def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname, 'イギリス').split('\n')
    print(len(text))

    # カテゴリの行を表示する
    for line in text:
        if is_category(line):
            print(line, end=' : ')
            print(get_category_name(line))


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
