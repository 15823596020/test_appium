from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.add_member_info_page import AddMemberInfoPage
from test_appium.test_wechat.page.basepage import BasePage

class AddMemberPage(BasePage):  # 继承BasePage类
    # 点击手动输入添加，进入添加成员信息页
    def manual_input_add(self):
        self.find(MobileBy.XPATH, "//*[contains(@text,'手动输入')]").click()  # 点击手动输入添加
        return AddMemberInfoPage(self._driver)  # 实例化AddMemberInfoPage，进入添加成员信息页

    # 获取toast
    def get_toast(self):
        # print(self._driver.page_source)  # 打印当前页面的内容
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text  # 定位toast并返回toast的text
