from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.basepage import BasePage
from test_appium.test_wechat.page.edit_member_page import EditMember

class EditMessagePage(BasePage):  # 继承BasePage类
    # 点击编辑成员按钮，进入编辑成员页
    def edit_member(self):
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()  # 点击编辑成员
        return EditMember(self._driver)  # 实例化EditMember，进入编辑成员页
