# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: 
# @Time   : 2024-03-17 19:50
# @Author : 毛鹏
from auto_test.api.wan_android import WanAndroidDataModel
from models.api_model import ApiDataModel
from tools.base_request.request_tool import RequestTool
from tools.decorator.response import request_data


class LoginAPI(RequestTool):
    data_model = WanAndroidDataModel()

    @request_data(1)
    async def api_login(self, data: ApiDataModel) -> ApiDataModel:
        """
        登录接口
        @param data: ApiDataModel
        @return: ApiDataModel
        """
        return await self.http(data)

    async def api_reset_password(self) -> ApiDataModel:
        pass
