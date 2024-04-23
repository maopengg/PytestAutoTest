# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-08-11 11:08
# @Author : 毛鹏
# ↓-----------------------------------数据源选择-----------------------------------↓
from enums.tools_enum import SourcesTypeEnum

SOURCES_TYPE = SourcesTypeEnum.DOCUMENT

# ↑-----------------------------------数据源选择-----------------------------------↑

# ↓-----------------------------------飞书共享文档数据源-----------------------------------↓
APP_ID = "cli_a680e4c8c5be100c"
APP_SECRET = "uKEDeCAamlviajfBrxXjBhiSKnxONf6x"
API_INFO = ("LntEsBf88h8KDXtjmKNcHgwSnoc", [{"sheet_id": "ef820e", "title": "Sheet1"}])
API_TEST_CASE = ("XLcrsEVLkhdDQvtWaJQc4uennvb", [{"sheet_id": "e8f425", "title": "Sheet1"}])
PROJECT = ("StFhs7b34h410ktn4FBc9qJsn8e", [{"sheet_id": "8d41b9", "title": "项目信息"},
                                           {"sheet_id": "58AgAa", "title": "通知配置"},
                                           {"sheet_id": "RwlKtG", "title": "测试环境"}])
UI_ELEMENT = ("ZQfZsC7IShpkGytZLoKc1gbXnPS", [{"sheet_id": "9f326e", "title": "Sheet1"}])

# ↑-----------------------------------飞书共享文档数据源-----------------------------------↑
# ↓-----------------------------------API自动化配置-----------------------------------↓

PRINT_EXECUTION_RESULTS = True  # 是否开启日志打印
REQUEST_TIMEOUT_FAILURE_TIME = 60  # 请求超时失败时间

# ↑-----------------------------------API自动化配置-----------------------------------↑
# ↓-----------------------------------UI自动化配置-----------------------------------↓

BROWSER_IS_MAXIMIZE = True  # 是否开启UI自动化浏览器全屏

# ↑-----------------------------------UI自动化配置-----------------------------------↑
# ↓-----------------------------------邮件配置-----------------------------------↓

EMAIL_HOST = 'smtp.qq.com'  # 发送邮件host，这个是QQ邮箱
SEND_USER = '729164035@qq.com'  # 发送用户
STAMP_KEY = 'lqfzvjbpfcwtbecg'  # 用户的key

# ↑-----------------------------------邮件配置-----------------------------------↑
# ↓-----------------------------------全局请求代理设置-----------------------------------↓

PROXY = {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890'}  # 代理地址，如果没有就是空字典
# 'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890'
# ↑-----------------------------------全局请求代理设置-----------------------------------↑
# ↓-----------------------------------是否在运行结束后生成报告-----------------------------------↓

IS_TEST_REPORT = True
# ↑-----------------------------------是否在运行结束后生成报告-----------------------------------↑


if __name__ == '__main__':
    print("is_Test_Report".upper())
