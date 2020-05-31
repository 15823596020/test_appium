from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.basepage import BasePage

class EditMember(BasePage):  # 继承BasePage类
    # 编辑姓名
    def edit_name(self):
        return self  # 编辑姓名后，返回自己

    # 编辑性别
    def edit_gender(self):
        return self  # 编辑性别后，返回自己

    # 编辑电话
    def edit_phonenum(self):
        return self  # 编辑电话后，返回自己

    # 点击删除成员按钮，然后点击弹框中的确定按钮，就删除该成员
    def delete_name(self):
        # 这里需要局部导入，因为确定删除成员后，会返回通讯录页，所以需要局部导入。否则会因为循环导入而报错
        from test_appium.test_wechat.page.address_page import AddressPage

        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()  # 点击删除成员
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()  # 点击确定
        return AddressPage(self._driver)