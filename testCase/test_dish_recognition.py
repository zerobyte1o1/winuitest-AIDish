import os
from datetime import datetime

from handlers.meals_pricing_handler import MealsPricingHandler
import allure
import pytest


@allure.epic("模块：菜品计价")
@allure.feature("场景：菜品识别操作")
class TestDishRecognition:
    def setup_class(self):
        self.mph = MealsPricingHandler()
        with allure.step('打开需要识别的图片'):
            self.mph.click_open_img_loc()
            current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            img_path = os.path.join(current_path, "data", "test_img.jpg")
            self.mph.type_keys_open_img_file_name_loc(img_path)
            self.mph.click_open_img_ok_loc()

    def setup(self):
        with allure.step('点击重新识别'):
            self.mph.click_reidentify_loc()

    def teardown(self):
        self.mph.app.kill(self.mph.process_id)

    @allure.story("菜品新增操作")
    @allure.title("新增菜品_确定")
    @allure.description("识别菜品并新增菜品")
    @allure.testcase(
        "http://192.168.10.26:8081/#/track/case/edit/84680bbd-c131-e114-8dcc-20cbb5364230?projectId=9f25fcce-03ea-40a6-a911-e736e7af30ed",
        name="点击，跳转到对应用例的链接地址")
    @pytest.mark.p0
    def test_clear_machine_forward(self):
        pass
