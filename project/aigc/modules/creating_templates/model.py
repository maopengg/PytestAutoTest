# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-08-08 11:25
# @Author : 毛鹏
from pydantic import BaseModel


class CreatingTemplatesModel(BaseModel):
    createTime: str
    updateTime: str
    id: int
    accountId: str
    accountName: str
    brandName: str
    marketingTarget: str
    grade: str
    business: str
    firstLevel: str
    secondLevel: str
    kpis: str | None
    userId: int
    user: str
    status: int


class SonMote2Model(BaseModel):
    id: int
    name: str
    preset: int
    pid: int


class SonMote1Model(BaseModel):
    id: int
    name: str
    preset: int
    children: list[SonMote2Model] | None
    pid: int


class MoteModel(BaseModel):
    id: int
    name: str
    preset: int
    children: list[SonMote1Model] | None
    pid: int


class ResponseModel(BaseModel):
    data: list[CreatingTemplatesModel | MoteModel] | None | str
    status: int
    message: str | None

    @classmethod
    def get_obj(cls, result: dict):
        return cls(status=result.get('status'),
                   message=result.get('message'),
                   data=result.get('data'))