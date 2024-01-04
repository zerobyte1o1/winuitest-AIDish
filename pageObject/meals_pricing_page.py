from pageObject.base_page import BasePage


class MealsPricingPage(BasePage):
    def __init__(self):
        super(MealsPricingPage, self).__init__()

    def order_mgr_loc(self):
        """
        获取订单管理元素
        """
        return self.locate_element(title='订单')

    def food_management_loc(self):
        """
        获取菜品管理元素
        """
        return self.locate_element(title='菜品')

    def open_img_loc(self):
        """
        获取打开图片元素
        """
        return self.locate_element(title='打开')

    def open_img_file_name_loc(self):
        """
        获取打开图片文件名元素
        """
        return self.locate_element(auto_id="1148")

    def open_img_ok_loc(self):
        """
        获取打开图片确定元素
        """
        return self.locate_element(auto_id="1",title="打开(O)")

    def open_img_no_loc(self):
        """
        获取打开图片取消元素
        """
        return self.locate_element(auto_id="2")

    def clear_machine_loc(self):
        """
        获取清机元素
        """
        return self.locate_element(title='清机')

    def clear_machine_tips_loc(self):
        """
        获取清机提示元素
        """
        return self.locate_element(title_re="^上次清机时间.*")

    def clear_machine_yes_loc(self):
        """
        获取清机确定元素
        """
        return self.locate_element(auto_id='PageBase.widgetMain.CashierWidget.SFMessageForm.btnOk')

    def clear_machine_no_loc(self):
        """
        获取清机取消元素
        """
        return self.locate_element(auto_id='PageBase.widgetMain.CashierWidget.SFMessageForm.btnCancel')

    def digital_selection_loc(self):
        """
        获取数字点选元素
        """
        return self.locate_element(title="数字点选")

    def drink_loc(self):
        """
        获取酒水饮料元素
        """
        return self.locate_element(title="酒水饮料")

    def non_standard_loc(self):
        """
        获取非标品元素
        """
        return self.locate_element(title="非标品")

    def calculation_loc(self, digit: str):
        """
        定位数字键盘输入
        :param digit:str
        :return:
        """
        return self.locate_element(title=digit)

    def reidentify_loc(self):
        """
        获取重新识别元素
        """
        return self.locate_element(title="重新\n识别")

    def merged_payment_loc(self):
        """
        获取合并支付元素
        """
        return self.locate_element(title="合并\n支付")

    def auto_payment_loc(self):
        """
        获取自动支付元素
        """
        return self.locate_element(title="自动\n支付")

    def cash_payment_loc(self):
        """
        获取现金支付元素
        """
        return self.locate_element(title="现金\n支付")

    def cooperative_payment_loc(self):
        """
        获取合作支付元素
        """
        return self.locate_element(title="合作\n支付")

    def hanging_orders_loc(self):
        """
        获取挂起订单元素
        """
        return self.locate_element(title="挂起\n订单")

    def cancel_payment_loc(self):
        """
        获取取消支付元素
        """
        return self.locate_element(title="取消\n支付")

    def confirm_payment_loc(self):
        """
        获取确认支付元素
        """
        return self.locate_element(title="确认支付")

    def identification_of_areas_loc(self):
        """
        获取区域识别元素
        """
        return self.locate_element(class_name="QImageViewer")

    def total_amount_loc(self):
        """
        获取总金额元素
        """
        return self.locate_element(class_name="QPushButton", found_index=1)

    def promotion_amount_loc(self):
        """
        获取促销金额元素
        """
        return self.locate_element(class_name="QPushButton", found_index=2)
