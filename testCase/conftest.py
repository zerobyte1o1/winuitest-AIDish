from utils.wechat_info import send_wechat_message
import pytest


@pytest.fixture(scope='session')
def send_info():
    """
    发送企业微信消息
    :return:
    """
    yield
    send_wechat_message()

send_wechat_message()