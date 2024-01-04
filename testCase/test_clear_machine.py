from datetime import datetime

from handlers.meals_pricing_handler import MealsPricingHandler
import allure
import pytest


@allure.epic("模块：菜品计价")
@allure.feature("场景：操作清机")
class TestClearMachine:
    def setup_class(self):
        self.mph = MealsPricingHandler()

    def teardown(self):
        self.mph.app.kill(self.mph.process_id)

    @allure.story("操作清机")
    @allure.title("清机_确认")
    @allure.description("该用例检查用户确认清机操作")
    @allure.testcase("http://192.168.10.26:8081/#/track/case/edit/2705207b-92ca-03c4-60b2-23230d424de3?projectId=9f25fcce-03ea-40a6-a911-e736e7af30ed", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.p0
    def test_clear_machine_forward(self):
        with allure.step('点击清机按钮'):
            self.mph.click_clear_machine_loc()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with allure.step('点击确定'):
            self.mph.click_clear_machine_yes_lco()
        with allure.step('再次点击清机按钮'):
            self.mph.click_clear_machine_loc()
        with allure.step('校验是否已清机成功'):
            assert current_time in self.mph.text_clear_machine_tips_loc()

    @allure.story("操作清机")
    @allure.title("清机_取消")
    @allure.description("该用例检查用户取消清机操作")
    @allure.testcase("http://192.168.10.26:8081/#/track/case/edit/45f9032c-8167-1c5c-8705-69cbd4eae7d5?projectId=9f25fcce-03ea-40a6-a911-e736e7af30ed", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.p2
    def test_clear_machine_reverse(self):
        with allure.step('点击清机按钮'):
            self.mph.click_clear_machine_loc()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with allure.step('点击取消'):
            self.mph.click_clear_machine_no_lco()
        with allure.step('再次点击清机按钮'):
            self.mph.click_clear_machine_loc()
        with allure.step('校验是否已清机成功'):
            assert current_time not in self.mph.text_clear_machine_tips_loc()
