# coding: utf-8

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import gzip
import json


def read_wiki(fname, title):
    """指定のタイトルの記事本文を表示する。
    """
    #  ファイルを解凍して読み込む
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            # titleを比較する
            if data_json['title'] == title:
                return data_json['text']


def main():
    fname = 'jawiki-country.json.gz'
    print(read_wiki(fname, 'イギリス'))

if __name__ == '__main__':
    main()
