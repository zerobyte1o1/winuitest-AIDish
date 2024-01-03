from pageObject.meals_pricing_page import MealsPricingPage
from utils.logger import log_decorator


class MealsPricingHandler(MealsPricingPage):
    """
    菜品计价页面
    """

    def __init__(self):
        super(MealsPricingHandler, self).__init__()

    def click_clear_machine_loc(self):
        self.clear_machine_loc().click()

    def click_clear_machine_yes_lco(self):
        self.clear_machine_yes_loc().click()

    def click_clear_machine_no_lco(self):
        self.clear_machine_no_loc().click()

    def click_digital_selection_loc(self):
        self.digital_selection_loc().click()

    def click_drink_loc(self):
        self.drink_loc().click()

    def click_non_standard_loc(self):
        self.non_standard_loc().click()

    def click_calculation_loc(self, digit: str):
        self.calculation_loc(digit).click()

    def click_reidentify_loc(self):
        self.reidentify_loc().click()

    def click_merged_payment_loc(self):
        self.merged_payment_loc().click()

    def click_auto_payment_loc(self):
        self.auto_payment_loc().click()

    def click_cash_payment_loc(self):
        self.cash_payment_loc().click()

    def click_cooperative_payment_loc(self):
        self.cooperative_payment_loc().click()

    def click_hanging_orders_loc(self):
        self.hanging_orders_loc().click()

    def click_cancel_payment_loc(self):
        self.cancel_payment_loc().click()

    def click_confirm_payment_loc(self):
        self.confirm_payment_loc().click()

    def click_identification_of_areas_loc(self):
        self.identification_of_areas_loc().click_input()

    def text_total_amount_loc(self):
        return self.total_amount_loc().window_text()

if __name__ == '__main__':
    a=MealsPricingHandler().text_total_amount_loc()
    print(a)
