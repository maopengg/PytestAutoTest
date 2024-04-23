# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2024-04-23 11:27
# @Author : 毛鹏
import allure
import pytest

from auto_test.api.mango_testing_platform.modules_api.ui_auto.page_element import PageElementAPI
from models.api_model import ApiDataModel
from tools.base_request.case_tool import CaseTool
from tools.data_processor import DataProcessor
from tools.decorator.response import case_data


@allure.epic('芒果测试平台')
@allure.feature('页面对象')
class TestPageElement(PageElementAPI, CaseTool):
    data_processor: DataProcessor = DataProcessor()

    @allure.title('获取type等于0的页面对象列表')
    @allure.description('测试页面元素的列表')
    @case_data(7)
    def test_login01(self, data: ApiDataModel):
        data = self.page_element_list(data)
        assert data.response.response_dict['code'] == 200, f"断言失败：返回的code不是200，{data.response.response_dict}"
        assert data.response.response_dict['data'] is not None


if __name__ == '__main__':
    pytest.main(
        [
            r'D:\GitCode\PytestAutoTest\auto_test\api\mango_testing_platform\test_case\test_login.py::TestLogin::test_login01']
    )