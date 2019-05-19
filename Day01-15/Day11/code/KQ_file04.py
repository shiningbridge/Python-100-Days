###
# Test file operations and exceptions.
# Path: Day11/code/
# Created Date: Saturday May 18th 2019
# Author: Kangqiao
# -----
# Last Modified: 2019-05-18 22:56:33
# Modified By: the developer formerly known as Kangqiao at <shiningbridge@gmail.com>
# -----
# Copyright (c) 2019 NanFei
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2019-05-18	KQ	加入base64的编码和解码。以及try， except处理异常。。。
###


import base64


def main():
    try:
        with open('Day1/code/mm.jpg', 'rb') as f:
            data = f.read()
            print(type(data))
            # print(data)
            print('Bytes: %s' % len(data))

            # 将图片处理成BASE-64编码
            data64 = base64.b64encode(data)
            # print(data64)
        print('编码完成!')

        with open('Day11/code/bb.jpg', 'wb') as f:
            f.write(base64.b64decode(data64))
        print('写入完成!')
    except FileNotFoundError as e:
        print('这文件打不开', e)
    except IOError:
        print('读写出问题啦')
    print('但是程序还是能到这一步的！！！')


if __name__ == "__main__":
    main()
