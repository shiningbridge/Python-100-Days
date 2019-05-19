###
# Test file operations and exceptions.
# Path: Day11/code/
# Created Date: Saturday May 18th 2019
# Author: Kangqiao
# -----
# Last Modified: 2019-05-18 23:31:09
# Modified By: the developer formerly known as Kangqiao at <shiningbridge@gmail.com>
# -----
# Copyright (c) 2019 NanFei
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2019-05-18	KQ	json和python字典的对应关系。
###

import json

def main():
    teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
    json_str = json.dumps(teacher_dict)
    print(json_str)
    print(type(json_str))
    fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
    json_str = json.dumps(fruits_list)
    print(json_str)
    print(type(json_str))

    # try:
    #     with open('Day1/code/mm.jpg', 'rb') as f:
            
    # except FileNotFoundError as e:
    #     print('这文件打不开', e)
    # except IOError:
    #     print('读写出问题啦')
    # print('但是程序还是能到这一步的！！！')


if __name__ == "__main__":
    main()
