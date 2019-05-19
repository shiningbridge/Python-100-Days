###
# Test file operations and exceptions.
# Path: Day11/code/
# Created Date: Saturday May 18th 2019
# Author: Kangqiao
# -----
# Last Modified: 2019-05-18 22:37:43
# Modified By: the developer formerly known as Kangqiao at <shiningbridge@gmail.com>
# -----
# Copyright (c) 2019 NanFei
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
###


from math import sqrt


def is_prime(n):
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True


def main():
    # 试一试有什么不一样
    # with open('prime.txt', 'a') as f:
    # with open('prime.txt', 'w') as f:
    with open('Day11/code/prime.txt', 'w') as f:
        for num in range(2, 100):
            if is_prime(num):
                f.write(str(num) + '\n')
    print('写入完成!')


if __name__ == "__main__":
    main()
