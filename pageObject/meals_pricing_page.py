from pageObject.base_page import BasePage


class MealsPricingPage(BasePage):
    def __init__(self):
        super(MealsPricingPage, self).__init__()

    def order_mgr_loc(self):
        return self.locate_element(title='订单')

    def food_management_loc(self):
        return self.locate_element(title='菜品')

    def clear_machine_loc(self):
        return self.locate_element(title='清机')

    def clear_machine_tips_loc(self):
        return self.locate_element(auto_id="PageBase.widgetMain.CashierWidget.SFMessageForm.widgetMsg.lbMsg")

    def clear_machine_yes_loc(self):
        return self.driver['提示'].child_window(auto_id='PageBase.widgetMain.CashierWidget.SFMessageForm.btnOk')

    def clear_machine_no_loc(self):
        return self.locate_element(auto_id='PageBase.widgetMain.CashierWidget.SFMessageForm.btnCancel')

    def digital_selection_loc(self):
        return self.locate_element(title="数字点选")

    def drink_loc(self):
        return self.locate_element(title="酒水饮料")

    def non_standard_loc(self):
        return self.locate_element(title="非标品")

    def calculation_loc(self, digit: str):
        """
        定位数字键盘输入
        :param digit:str
        :return:
        """
        return self.locate_element(title=digit)

    def reidentify_loc(self):
        return self.locate_element(title="重新\n识别")

    def merged_payment_loc(self):
        return self.locate_element(title="合并\n支付")

    def auto_payment_loc(self):
        return self.locate_element(title="自动\n支付")

    def cash_payment_loc(self):
        return self.locate_element(title="现金\n支付")

    def cooperative_payment_loc(self):
        return self.locate_element(title="合作\n支付")

    def hanging_orders_loc(self):
        return self.locate_element(title="挂起\n订单")

    def cancel_payment_loc(self):
        return self.locate_element(title="取消\n支付")

    def confirm_payment_loc(self):
        return self.locate_element(title="确认支付")

    def identification_of_areas_loc(self):
        return self.locate_element(class_name="QImageViewer")

    def total_amount_loc(self):
        return self.locate_element(class_name="QPushButton", found_index=1)

    def promotion_amount_loc(self):
        return self.locate_element(class_name="QPushButton", found_index=2)
