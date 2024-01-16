from utils.wechat_info import send_wechat_message
import pytest


@pytest.fixture(scope='session',autouse=True)
def send_info(request):
    """
    发送企业微信消息
    :return:
    """

    request.addfinalizer(send_wechat_message)
