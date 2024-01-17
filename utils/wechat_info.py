from utils.env import env
from utils.logger import log
import requests
import os


def send_wechat_message():
    try:
        with open(env.get_listen_file(), "r") as file:
            version = file.readline().strip()
    except FileNotFoundError:
        log.warning("no listen file")
        
    parent_directory = os.path.dirname(os.path.dirname(os.getcwd()))
    result_file = os.path.join(parent_directory, "result.txt")
    
    with open(result_file, "r") as fp:
        lines = fp.readlines()
        if lines[5].split("=")[1].strip() == "100%":
            title = "通过"
        else:
            title = "未通过"
        content = ""
        for line in lines:
            content += "<p>" + line.strip() + "</p>\n"
             
    content = "<font color=\"warning\">"+version+"自动化测试"+title+"</font>\n >[详细报告](" + env.get_report_url() + ")"+content
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
