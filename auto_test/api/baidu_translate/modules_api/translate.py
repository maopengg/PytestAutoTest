# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: 
# @Time   : 2024-03-17 19:50
# @Author : 毛鹏

from auto_test.api.baidu_translate import BaiduTranslateModel
from models.api_model import ApiDataModel
from tools.base_request.request_tool import RequestTool
from tools.decorator.response import request_data


class TranslateApi(RequestTool):
    data_model: BaiduTranslateModel = BaiduTranslateModel()

    @request_data(2)
    async def translate(self, data: ApiDataModel = None):
        return await self.http(data)


if __name__ == '__main__':
    TranslateApi().translate()
