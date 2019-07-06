#!/usr/bin/env python
# -*- coding：utf-8 -*-
'''
@author: maya
@contact: 1278077260@qq.com
@software: Pycharm
@file: test.py
@time: 2019/4/11 9:21
@desc:
'''
import re
def num_format(num):
    tmp_num = ('%s' % (num*100))
    num_index = tmp_num.index(re.findall('[1-9]', tmp_num.split('.')[1])[0])
    return float(tmp_num[:num_index + 1])

if __name__ == '__main__':
    print(num_format(0.003))
    print(num_format(0.00003))