from utils.env import env
from utils.logger import log
import requests


def send_wechat_message():
    content = "<font color=\"warning\">自动化测试已完成</font>\n >[测试报告](" + env.get_report_url() + ")"
    body = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    try:
        response = requests.post(env.get_info_url(), json=body, headers=headers)
        log.info(response.text)
    except Exception as e:
        log.warning("发送企业微信消息出错"+e)
    # print(response.status_code)
    # print(response.content)
    # print(response.text)
