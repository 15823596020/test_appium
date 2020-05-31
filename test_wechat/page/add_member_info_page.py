from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.basepage import BasePage

class AddMemberInfoPage(BasePage):  # 继承BasePage类
    # 输入姓名
    def set_name(self, name):
        self.find(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys(name)  # 定位姓名输入框，并输入姓名
        return self  # 输入姓名后，返回自己

    # 选择性别
    def set_gender(self, gender):
        self.find(MobileBy.XPATH, "//*[@text='男']").click()  # 点击性别
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()  # 点击选择性别
        return self  # 输入性别后，返回自己

    # 输入手机号
    def set_phonenum(self, phone):
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机') and contains(@class,'TextView')]/..//*[@text='手机号']").send_keys(phone)  # 定位手机号输入框，并输入手机号
        return self  # 输入手机号后，返回自己

    # 点击保存
    def click_save(self):
        # 这里需要局部导入，因为添加成员页，点击手动输入添加后，进入到了这一页，这一页保存后返回上一页，需要局部导入。否则会因为循环导入而报错
        from test_appium.test_wechat.page.add_member_page import AddMemberPage

        self.find(MobileBy.XPATH, "//*[@text='保存']").click()  # 点击保存按钮
        return AddMemberPage(self._driver)  # 点击保持后，返回AddMemberPage添加成员页