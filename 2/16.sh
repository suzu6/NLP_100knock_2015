#!/bin/sh

# Nを入力
echo -n "N--> "
read n

# 行数算出　wcは行数とファイル名を出力するのでcutで行数のみ切り出し
count=`wc --line hightemp.txt | cut --fields=1 --delimiter=" "`

# 1分割当たりの行数算出　余りがある場合は行数を+1
unit=`expr $count / $n`
remainder=`expr $count % $n`
if [ $remainder -gt 0 ]; then
    unit=`expr $unit + 1`
fi

# 分割
split --lines=$unit --numeric-suffixes=1 --additional-suffix=.txt hightemp.txt child_test_
