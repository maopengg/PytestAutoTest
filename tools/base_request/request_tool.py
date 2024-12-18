# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-09-04 17:23
# @Author : 毛鹏

from urllib.parse import urljoin

from mangokit import requests, DataProcessor
from requests.models import Response

from models.api_model import ApiDataModel, RequestModel, ResponseModel
from tools.decorator.response import timer, log_decorator
from tools.log_collector import log

class RequestTool:
    data_processor: DataProcessor = None

    @log_decorator
    async def http(self, data: ApiDataModel) -> ApiDataModel | Response:
        """
        处理请求的数据，写入到request对象中
        @return:
        """
        data.request.url = urljoin(data.base_data.host, data.request.url)
        for key, value in data.request:
            if value is not None and key != 'file':
                value = self.data_processor.replace(value)
                setattr(data.request, key, value)
            elif key == 'file':
                if data.request.file:
                    file = []
                    for i in data.request.file:
                        i: dict = i
                        for k, v in i.items():
                            file_name = self.data_processor.identify_parentheses(v)[0].replace('(', '').replace(')', '')
                            path = self.data_processor.replace(v)
                            file.append((k, (file_name, open(path, 'rb'))))
                    data.request.file = file
        data.response = await self.http_request(data.request)
        log.warning(data.response)
        return data

    @timer
    async def http_request(self, request_model: RequestModel) -> ResponseModel | Response:
        """
        全局请求统一处理
        @param request_model: RequestDataModel
        @return: ApiDataModel
        """
        return requests.request(
            method=request_model.method,
            url=request_model.url,
            headers=request_model.headers,
            params=request_model.params,
            data=request_model.data,
            json=request_model.json_data,
            files=request_model.file,
        )

    @staticmethod
    def internal_http(url: str,
                      method: str,
                      headers: dict | None = None,
                      params: dict | None = None,
                      data: str | dict | None = None,
                      json: dict | None = None,
                      file: dict | None = None) -> Response:
        """
        内部使用的全局请求统一处理
        @return: ApiDataModel
        """
        data = RequestModel(
            url=url,
            method=method,
            headers=headers,
            params=params,
            data=data,
            json_data=json,
            file=file,
        )
        return requests.request(
            method=data.method,
            url=data.url,
            headers=data.headers,
            params=data.params,
            data=data.data,
            json=data.json_data,
            files=data.file,
        )
