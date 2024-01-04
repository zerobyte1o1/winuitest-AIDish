from pageObject.meals_pricing_page import MealsPricingPage
from utils.logger import Logger


class MealsPricingHandler(MealsPricingPage):
    """
    菜品计价页面
    """

    def __init__(self):
        super(MealsPricingHandler, self).__init__()

    def click_clear_machine_loc(self):
        """
        点击清机按钮
        """
        self.clear_machine_loc().click_input()

    def click_clear_machine_yes_lco(self):
        """
        点击确定按钮
        """
        self.clear_machine_yes_loc().click_input()

    def click_clear_machine_no_lco(self):
        """
        点击取消按钮
        """
        self.clear_machine_no_loc().click_input()

    def click_open_img_loc(self):
        """
        点击打开图片按钮
        """
        self.open_img_loc().click_input()

    def set_text_open_img_file_name_loc(self, path):
        """
        设置打开图片文件名
        """
        self.open_img_file_name_loc().set_text(path)

    def click_open_img_ok_loc(self):
        """
        点击打开图片确定按钮
        """
        self.open_img_ok_loc().click_input()

    def click_open_img_no_loc(self):
        """
        点击打开图片取消按钮
        """
        self.open_img_no_loc().click_input()

    def text_clear_machine_tips_loc(self):
        """
        获取清机提示文本
        """
        return self.clear_machine_tips_loc().window_text()

    def click_digital_selection_loc(self):
        """
        点击数字选择按钮
        """
        self.digital_selection_loc().click_input()

    def click_drink_loc(self):
        """
        点击饮料按钮
        """
        self.drink_loc().click_input()

    def click_non_standard_loc(self):
        """
        点击非标按钮
        """
        self.non_standard_loc().click_input()

    def click_calculation_loc(self, digit: str):
        """
        点击计算按钮
        :param digit: 数字
        """
        self.calculation_loc(digit).click_input()

    def click_reidentify_loc(self):
        """
        点击重新识别按钮
        """
        self.reidentify_loc().click_input()

    def click_merged_payment_loc(self):
        """
        点击合并支付按钮
        """
        self.merged_payment_loc().click_input()

    def click_auto_payment_loc(self):
        """
        点击自动支付按钮
        """
        self.auto_payment_loc().click_input()

    def click_cash_payment_loc(self):
        """
        点击现金支付按钮
        """
        self.cash_payment_loc().click_input()

    def click_cooperative_payment_loc(self):
        """
        点击合作支付按钮
        """
        self.cooperative_payment_loc().click_input()

    def click_hanging_orders_loc(self):
        """
        点击挂单按钮
        """
        self.hanging_orders_loc().click_input()

    def click_cancel_payment_loc(self):
        """
        点击取消支付按钮
        """
        self.cancel_payment_loc().click_input()

    def click_confirm_payment_loc(self):
        """
        点击确认支付按钮
        """
        self.confirm_payment_loc().click_input()

    def click_identification_of_areas_loc(self):
        """
        点击区域识别按钮
        """
        self.identification_of_areas_loc().click_input()

    def text_total_amount_loc(self):
        """
        获取总金额文本
        :return:
        """
        return self.total_amount_loc().window_text()

    def text_promotion_amount_loc(self):
        """
        获取优惠金额文本
        :return:
        """
        return self.promotion_amount_loc().window_text()


if __name__ == '__main__':
    print("开始")
    log = Logger().logger
    a = MealsPricingHandler()
    a.click_open_img_loc()
    current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path=os.path.join(current_path, "/data/test_img.jpg")
    print(img_path)
    a.set_text_open_img_file_name_loc(img_path)
    a.click_open_img_ok_loc()
