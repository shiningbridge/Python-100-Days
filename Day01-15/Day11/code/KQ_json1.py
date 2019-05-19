###
# Test file operations and exceptions.
# Path: Day11/code/
# Created Date: Saturday May 18th 2019
# Author: Kangqiao
# -----
# Last Modified: 2019-05-18 23:29:34
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
import csv2

def main():
    json_str = '{"name": "菲菲", "age": 38, "title": "二阶导"}'
    result = json.loads(json_str)
    print(result)
    print(type(result))
    print(result["name"])
    print(result["age"])

    # 把转换得到的字典作为关键字参数传入Teacher的构造器
    teacher = csv2.Teacher(**result)
    print(teacher)
    print(teacher.name)
    print(teacher.age)
    print(teacher.title)

    # try:
    #     with open('Day1/code/mm.jpg', 'rb') as f:
            
    # except FileNotFoundError as e:
    #     print('这文件打不开', e)
    # except IOError:
    #     print('读写出问题啦')
    # print('但是程序还是能到这一步的！！！')


if __name__ == "__main__":
    main()
