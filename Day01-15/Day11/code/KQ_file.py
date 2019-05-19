###
# Test file operations and exceptions.
#
# Created Date: Saturday May 18th 2019
# Author: Kangqiao
# -----
# Last Modified: 2019-05-18 22:27:27
# Modified By: the developer formerly known as Kangqiao at <shiningbridge@gmail.com>
# -----
# Copyright (c) 2019 NanFei
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
#
# 2019-05-18	KQ	从文本文件中读取数据
###


import time


def main():
    with open('Day11/code/致橡树.txt', 'r') as f:
        print(f.read())

    with open('Day11/code/致橡树.txt', mode='r') as f:
        for l in f:
            print(l, end='')
            time.sleep(.5)
    print()  # 不然最后有个乱码%符号，没有换行。

    with open('Day11/code/致橡树.txt', 'r') as f:
        lines = f.readlines()
    print(lines)    # 不好看。
    for l in lines:
        print(l, end='')
    print()


if __name__ == "__main__":
    main()
