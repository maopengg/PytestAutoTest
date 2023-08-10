# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2022-12-04 17:14
# @Author : 毛鹏
from pydantic import BaseModel


class RequestModel(BaseModel):
    """请求"""
    case_id: int
    case_name: str
    url: str
    method: str
    headers: str | None
    body_type: int = None
    body: dict | str = None


class ApiCaseGroupModel(BaseModel):
    group_name: str
    case_group_list: list[RequestModel]


class ResponseModel(BaseModel):
    case_id: int
    case_name: str
    url: str
    method: str
    headers: dict
    response_time: float
    res_code: int
    body_type: int = None
    body: dict = None
    response: dict
    assertion_res: bool = None

    @classmethod
    def create_empty(cls):
        return cls(case_id=0, case_name="", url="", method="", headers={}, response_time=0.0,
                   res_code=100, body_type=0, body={}, assertion_res=False)


class ApiPublicModel(BaseModel):
    """api公共"""
    project_id: int
    client: int
    public_type: int
    name: str
    key: str
    value: str
    state: int
    type: int
