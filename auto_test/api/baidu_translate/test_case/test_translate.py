# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-08-08 15:30
# @Author : 毛鹏
import asyncio

import allure
import pytest
from mangokit import DataProcessor

from auto_test.api.baidu_translate.modules_api.translate import TranslateApi
from models.api_model import ApiDataModel
from tools.base_request.case_tool import CaseTool
from tools.decorator.response import case_data
from tools.log_collector import log


@allure.epic('演示-API自动化-第三方API-百度翻译')
@allure.feature('对接百度翻译接口')
class TestTranslate(TranslateApi, CaseTool):
    data_processor: DataProcessor = DataProcessor()

    @pytest.mark.asyncio
    @allure.title('英文翻译成中文')
    @case_data(4)
    async def test_01(self, data: ApiDataModel):
        log.info('123213')
        await asyncio.sleep(1)
        appid = self.data_model.cache_data.get('app_id')
        secret_key = self.data_model.cache_data.get('secret_key')
        salt = self.data_processor.randint(left=32768, right=65536)
        query = data.test_case.params.get('q')
        sign = self.data_processor.md5_32_small(data=appid + query + str(salt) + secret_key)
        data.test_case.params['appid'] = appid
        data.test_case.params['salt'] = salt
        data.test_case.params['sign'] = sign
        data = await self.translate(data)
        assert data.response.response_dict['trans_result'][0]['dst'] == "芒果"
        assert data.response.response_dict['trans_result'][0]['src'] == "mango"

    @pytest.mark.asyncio
    @allure.title('中文翻译成英文')
    @case_data(5)
    async def test_login02(self, data: ApiDataModel):
        appid = self.data_model.cache_data.get('app_id')
        secret_key = self.data_model.cache_data.get('secret_key')
        salt = self.data_processor.randint(left=32768, right=65536)
        query = data.test_case.params.get('q')
        sign = self.data_processor.md5_32_small(data=appid + query + str(salt) + secret_key)
        data.test_case.params['appid'] = appid
        data.test_case.params['salt'] = salt
        data.test_case.params['sign'] = sign
        data = await self.translate(data)
        assert data.response.response_dict['trans_result'][0]['src'] == "芒果"
        assert data.response.response_dict['trans_result'][0]['dst'] == "Mango"


if __name__ == '__main__':
    pytest.main(
        [r'D:\GitCode\PytestAutoTest\auto_test\api\baidu_translate\test_case\test_translate.py::TestTranslate'])
