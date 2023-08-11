# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-08-11 11:12
# @Author : 毛鹏
import base64
import hashlib
import json


class EncryptionOrEncodingTool:
    """加密或编码类"""

    @classmethod
    def md5_encrypt(cls, string: str) -> str:
        """
        对字符串进行MD5加密
        :param string:加密字符串
        :return:
        """
        # 创建一个MD5对象
        md5 = hashlib.md5()
        # 将字符串转换为字节流并进行加密
        md5.update(string.encode('utf-8'))
        # 获取加密后的结果
        encrypted_string = md5.hexdigest()
        return encrypted_string

    @classmethod
    def base64_encode(cls, data: str) -> str:
        """
        编码字符串
        :param data: 需要进行编码的字符串
        :return:
        """
        return base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')
