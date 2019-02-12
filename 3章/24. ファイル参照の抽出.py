# coding: utf-8

"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
[[File:Wikipedia-logo-v2-ja.png|thumb|説明文]]
"""


import gzip
import json
import re


def read_wiki(fname, tiltle):
    with gzip.open(fname, 'rt', encoding='UTF-8') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']


def is_file(string):
    return re.match(r'\[\[:*(ファイル|File):.*\]\]$', string)


def get_file_name(string):
    m = re.match(r'\[\[:*(ファイル|File):(.+?)\|.+\]\]$', string)
    # m.group(1) => '==='
    return m.group(2)


# ギャラリーに対応
def is_gallery_file(string):
    return re.match(r'^(ファイル|File):.*\]\]$', string)


def get_gallery_file(string):
    m = re.match(r'^(ファイル|File):(.+?)\|.+$', string)
    return m.group(2)

def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname, 'イギリス').split('\n')

    # カテゴリの行を表示する
    for line in text:
        # print(line)
        if is_file(line):
            print(get_file_name(line))
        elif is_gallery_file(line):
            print(get_gallery_file(line))


if __name__ == '__main__':
    main()
