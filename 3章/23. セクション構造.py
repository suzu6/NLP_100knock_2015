# coding: utf-8

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

1 : == セクションの見出し ==
2 : === サブセクションの見出し ===
3 : ==== サブサブセクションの見出し ====
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


def is_section(string):
    return re.match(r'^=+.+=+$', string)


def get_section_level(string):
    m = re.match(r'^(=+)(.+?)=+$', string)
    # m.group(1) => '==='
    return ' name : {0}\tlevel : {1} '.format(m.group(2), len(m.group(1)) - 1)


def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname, 'イギリス').split('\n')
    print(len(text))

    # カテゴリの行を表示する
    for line in text:
        if is_section(line):
            # print(line, end=' : ')
            print(get_section_level(line))


if __name__ == '__main__':
    main()
