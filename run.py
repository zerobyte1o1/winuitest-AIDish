import os.path
import subprocess
from utils.env import env
from utils.logger import log

try:
    with open(env.get_listen_file(), "r") as file:
        version = file.readline().strip()
except FileNotFoundError:
    log.warning("env.get_listen_file() no listen file")

subprocess.call(["allure-combine", "--auto-create-folders", "./result/allure-report", "--dest", "c:/allure-html/"+version])


