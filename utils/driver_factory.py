from pywinauto import Application
from utils.env import Environment
from utils.logger import Logger


class DriverFactory:
    # 静态属性
    driver = None
    log = None
    app = None

    @classmethod
    def get_driver(cls):
        env = Environment()
        app = Application(env.get_type())
        app.start(env.get_location())
        cls.app = app
        cls.driver = app[env.get_app_name()]
        cls.log = Logger().logger


if __name__ == '__main__':
    DriverFactory.get_driver()
