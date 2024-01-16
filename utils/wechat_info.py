from utils.env import env
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
        # response = requests.post(env.get_info_url(), json=body, headers=headers)
        print("执行了")
    except Exception as e:
        print("Error occurred while sending wechat message:", str(e))

    # print(response.status_code)
    # print(response.content)
    # print(response.text)

