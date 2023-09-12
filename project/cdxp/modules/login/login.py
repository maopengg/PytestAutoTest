# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-08-08 11:25
# @Author : 毛鹏
from requests.models import Response

from models.api_model import ApiInfoModel
from project.cdxp.cdxp_data_model import CDXPDataModel
from tools.data_processor import DataProcessor
from tools.decorator.response import around
from tools.request_tool.request_tool import RequestTool


class LoginAPI(DataProcessor, RequestTool):
    headers = {
        'Authorization': 'Basic d2ViQXBwOndlYkFwcA==',
        'Accept': 'application/json, text/plain, */*',
    }
    data_model: CDXPDataModel = CDXPDataModel()

    @classmethod
    @around(7)
    def api_login(cls, username, password, api_info: ApiInfoModel = None) -> tuple[Response, str, dict] | Response:
        """
        登录接口
        :return:
        """
        password = cls.md5_encrypt(password)
        url = f'{cls.data_model.host}{api_info.url}?username={username}&password={password}&grant_type=password_code'
        response = cls.http_post(url=url, headers=cls.headers)
        return response, url, cls.headers

    @classmethod
    @around(0)
    def api_reset_password(cls) -> tuple[Response, str, dict] | Response:
        """
        重置密码
        :return:
        """


if __name__ == '__main__':
    r = LoginAPI()
    print(r.api_login("", ""))
