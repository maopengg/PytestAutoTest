from pydantic import BaseModel, ConfigDict

from auto_test.project_enum import BaiduTranslateEnum
from enums.tools_enum import EnvironmentEnum
from models.api_model import ApiBaseDataModel
from mangokit import singleton, DataClean

from tools.log_collector import log
from tools.other.project_public_methods import ProjectPublicMethods


@singleton
class BaiduTranslateModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    user_info: dict | None = None
    headers: dict | None = None
    test_environment: int
    base_data_model: ApiBaseDataModel
    data_clean: DataClean = DataClean()
    cache_data: dict = {}


def data_init():
    """
    登录接口，获取通用token
    :return:
    """
    test_environment, project, test_object = ProjectPublicMethods.get_project_test_object(
        project_name=BaiduTranslateEnum.NAME.value,
        test_environment=EnvironmentEnum.PRO)
    mysql_config_model, mysql_connect = ProjectPublicMethods.get_mysql_info(test_object)
    data: BaiduTranslateModel = BaiduTranslateModel(
        test_environment=test_environment,
        base_data_model=ApiBaseDataModel(
            test_object=test_object,
            project=project,
            host=test_object.get('host'),
            is_database_assertion=bool(test_object.get('is_db')),
            mysql_config_model=mysql_config_model,
            mysql_connect=mysql_connect,
        )
    )
    data.cache_data['app_id'] = "20221117001456480"
    data.cache_data['secret_key'] = "YU2_BJkJoiiLRyBBkL0F"

    log.info(f'{BaiduTranslateEnum.NAME.value}的API在自动化基础信息设置完成！')


data_init()
