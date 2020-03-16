"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

内部リンク
[[記事名]]	記事名
[[記事名|表示文字]]	表示文字
[[記事名#節名|表示文字]]	表示文字
"""

# coding: utf-8

import gzip
import json
import re


def read_wiki(fname, tiltle):
    with gzip.open(fname, 'rt', encoding="utf-8") as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']


def get_basic_information(string):
    m1 = re.search(r'{{基礎情報 国.*?', string)
    # print(m1.end())
    m2 = re.search(r'(.*)\n}}\n', string[m1.end():])
    return string[m1.end():m2.end()+1]


def remove_emphasis(string):
    # 強調を除去
    # m = re.match(r"(.*)('{2,5})(.*?)(\2)(.*)", string) 何故か{2,5}で'がひとつ残る
    m = re.match(r"(.*)('{3,5})(.*?)(\2)(.*)", string)
    if m is None:
        return string
    dst = m.group(1) + m.group(3) + m.group(5)
    # print(dst)
    return dst


def main():
    fname = 'jawiki-country.json.gz'
    text = read_wiki(fname, 'イギリス')
    # print(len(text))
    text = get_basic_information(text).split('\n')

    basic_info = {}
    for line in text:
        m = re.match(r'\|(.+)( = )(.*)', line)
        if m is None:
            continue
        val = remove_emphasis(m.group(3).strip())
        basic_info[m.group(1).strip()] = val

    # JSONで表示を整形
    print(json.dumps(basic_info, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()
