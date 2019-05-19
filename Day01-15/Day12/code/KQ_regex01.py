###
# 验证输入用户名和QQ号是否有效并给出对应的提示信息

# 要求：
# 用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
# QQ号是5~12的数字且首位不能为0
# Created Date: Sunday May 19th 2019
# Author: Kangqiao
# -----
# Last Modified: 2019-05-19 23:20:36
# Modified By: the developer formerly known as Kangqiao at <shiningbridge@gmail.com>
# -----
# Copyright (c) 2019 NanFei
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2019-05-19	KQ	关键词过滤: 用到： re.sub
# 2019-05-19	KQ	电话号码筛选，保存到表中：用到：re.compile, re.findall
# 2019-05-19	KQ	QQ号匹配：用到：re.match
###

import re


def main():
    username = input('请输入用户名: ')   # 字母、数字或下划线构成且长度在6~20个字符之间
    qq = input('请输入QQ号: ')          # 5~12的数字且首位不能为0
    m1 = re.match(r'[a-zA-Z0-9_]{6,20}', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'[1-9][0-9]{4,11}', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')


    # 133/153/180/181/189/177
    # 130/131/132/155/156/185/186/145/176
    # 134/135/136/137/138/139/150/151/152/157/158/159/182/183/184/187/188/147/178
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r"""
    (?<=\D) # 非数字结尾之前的部分
    1       # 第一位 1
    [3-8]   # 第二位 3，4，5，6，7，8都有。
    \d{9}   # 后边9位，一共11位
    (?=\D)  # 非数字开头的零宽字符后边的部分
    """, re.X)
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

    ## 关键词过滤。
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)


if __name__ == '__main__':
    main()
