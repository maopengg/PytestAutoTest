# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-07-07 10:14
# @Author : 毛鹏
class AutoTestError(Exception):
    def __init__(self):
        self.code = None
        self.msg = None
