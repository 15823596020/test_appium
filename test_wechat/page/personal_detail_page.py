from appium.webdriver.common.mobileby import MobileBy
from test_appium.test_wechat.page.basepage import BasePage
from test_appium.test_wechat.page.edit_message_page import EditMessagePage

class PersonalDetailsPage(BasePage):  # 继承BasePage类
    # 点击邀请加入，发送邀请信息
    def invite_join(self):
        pass

    # 点击发消息，进入发送消息对话框页
    def send_message(self):
        pass

    # 点击语音通话，弹框，选择语音通话/视频通话
    def voice_communication(self):
        pass

    # 点击右上角的3个竖点，进入编辑个人信息页
    def goto_edit_message(self):
        self.find(MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//*[@resource-id='com.tencent.wework:id/gvr']").click()  # 点击右上角的三个点
        return EditMessagePage(self._driver)  # 实例化EditMessagePage类，进入编辑个人信息页