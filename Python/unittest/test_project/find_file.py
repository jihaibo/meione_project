#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-09 15:52:48
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

import os

# 定义文件目录
result_dir = 'D:\\testpro\\report'

lists = os.listdir(result_dir)

# 重新按时间对目录写的文件进行排序
lists.sort(key=lambda fn: os.path.getatime(result_dir+"\\"+fn))
print(('最新的文件为: ' + lists[-1]))
file = os.path.join(result_dir, lists[-1])
print(file)

