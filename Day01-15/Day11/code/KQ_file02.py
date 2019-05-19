###
# Test file operations and exceptions.
#
# Created Date: Saturday May 18th 2019
# Author: Kangqiao
# -----
# Last Modified: 2019-05-18 22:34:11
# Modified By: the developer formerly known as Kangqiao at <shiningbridge@gmail.com>
# -----
# Copyright (c) 2019 NanFei
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
###


def main():
    birth = input('请输入你的生日: ')
    with open('Day11/code/pi_million_digits.txt') as f:
        lines = f.readlines()
        pi_string = ''
        for line in lines:
            pi_string += line.strip()
        if birth in pi_string:
            print('Bingo!!!')


if __name__ == "__main__":
    main()
