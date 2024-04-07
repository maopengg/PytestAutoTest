# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description:
# @Time   : 2024-02-19 10:07
# @Author : 毛鹏
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2023/08/07 11:01
# @Author :
import os
from multiprocessing import Manager

import pytest

from auto_test.project_enum import ProjectTypePaths
from exceptions.error_msg import ERROR_MSG_0007
from exceptions.tools_exception import TestProjectError
from models.tools_model import CaseRunModel
from settings.settings import IS_TEST_REPORT
from tools.files.zip_files import zip_files
from tools.logging_tool import logger
from tools.notic_tools import NoticeMain
from tools.other_tools.native_ip import get_host_ip

shared_dict = None


class MainRun:

    def __init__(self, test_project: list[dict], pytest_command: list):
        self.data: list[CaseRunModel] = [CaseRunModel(**i) for i in test_project]
        self.pytest_command = pytest_command
        # 压缩上一次执行结果，并且保存起来，方便后面查询
        zip_files()
        self.run()

    def run(self):
        global shared_dict
        manager = Manager()
        shared_dict = manager.dict()
        project_type_paths = ProjectTypePaths()

        for case_run_model in self.data:
            project_key = case_run_model.project.value
            if project_key in project_type_paths.data:
                project_type_paths.set_test_environment(project_key, case_run_model.test_environment.value)
                # project_enum.project_type_paths[project_key]['test_environment'] = case_run_model.test_environment
                if case_run_model.type.value not in project_type_paths.data[project_key]:
                    raise TestProjectError(*ERROR_MSG_0007)
                if case_run_model.type.value in project_type_paths.data[project_key]:
                    self.pytest_command.append(project_type_paths.data[project_key][case_run_model.type.value])
            else:
                raise TestProjectError(*ERROR_MSG_0007)
        shared_dict['project_type_paths'] = project_type_paths

        logger.info(f'类ID:{id(project_type_paths)}')
        # 执行用例
        logger.info(f"开始执行测试任务......")
        pytest.main(self.pytest_command)
        # 发送通知
        NoticeMain(self.data).notice_main()
        if IS_TEST_REPORT:
            os.system(r"allure generate ./report/tmp -o ./report/html --clean")
            os.system(f"allure serve ./report/tmp -h {get_host_ip()} -p 9997")
