from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.add_member_page import AddMemberPage
from test_appium.test_wechat.page.basepage import BasePage
from test_appium.test_wechat.page.personal_detail_page import PersonalDetailsPage

class AddressPage(BasePage):  # 继承BasePage类
    # 点击添加成员，进入添加成员页
    def add_member(self):
        # 滚动查找添加成员，并点击
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return AddMemberPage(self._driver)  # 实例化AddMemberPage，进入添加成员页

    # 查找成员
    def search_member(self, name):
        # 滚动查找成员
        el_list = self.finds(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));')
        return el_list

    # 删除成员
    def delete_member(self, name):
        """
        1.查找需要删除的成员
        2.点击该成员，进入个人信息页
        :return:
        """
        # 滚动查找需删除的成员，并点击
        self.find(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));').click()
        return PersonalDetailsPage(self._driver)  # 实例化PersonalDetailsPage，进入个人信息页