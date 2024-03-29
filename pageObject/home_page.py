from pageObject.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        super(HomePage, self).__init__()
    def meals_pricing_loc(self):
        """
        获取菜品计价元素
        """
        return self.locate_element(title='菜品计价')

    def meals_management_loc(self):
        """
        获取菜品管理元素
        """
        return self.locate_element(title='菜品管理')

    def revenue_analysis_loc(self):
        """
        获取营收分析元素
        """
        return self.locate_element(title='营收分析')

    def member_management_loc(self):
        """
        获取会员管理元素
        """
        return self.locate_element(title='会员管理')

    def setting_loc(self):
        """
        获取设置元素
        """
        return self.locate_element(auto_id='PageBase.widgetTop.btnSetting')

    def min_loc(self):
        """
        获取最小化元素
        """
        return self.locate_element(auto_id='PageBase.widgetTop.btnMin')

    def close_loc(self):
        """
        获取关闭元素
        """
        return self.locate_element(auto_id='PageBase.widgetTop.btnClose')
