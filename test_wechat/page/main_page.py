from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.address_page import AddressPage
from test_appium.test_wechat.page.basepage import BasePage


class MainPage(BasePage):  # 继承BasePage类
    # 默认/点击，进入消息页
    def goto_message(self):
        pass

    # 点击通讯录，进入通讯录页
    def goto_address(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()  # 点击通讯录，进入通讯录页面
        return AddressPage(self._driver)  # 实例化AddressPage，进入添加成员页

    # 点击工作台，进入工作台页
    def goto_workbench(self):
        pass

    # 点击我，进入我页
    def goto_me(self):
        pass
