"""
课后作业
使用 Appium Inspector 录制企业微信搜索功能的测试用例，搜索一个存在的联系人。

用例步骤：
打开企业微信（提前登录）
进入通讯录
点击搜索按钮
输入 已存在的联系人姓名, 例如“aa”，
点击联系人，进入聊天页面
输入“测试code”
点击发送
退出应用
注意：

提前登录，绕过登录功能( 加 noReset 参数 设置为 True)
使用录制功能完成上面的功能，
进行简单的重构，使用 pytest 测试框架。
可以加入参数化，实现多条搜索功能的测试用例。
"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestWechat:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 平台
        desired_caps['platformVersion'] = '6.0'  # 平台版本
        desired_caps['deviceName'] = '127.0.0.1:7555'  # 设备名字
        desired_caps['appPackage'] = 'com.tencent.wework'  # 需要打开的包名
        desired_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'  # 打开APP的第一个activity
        desired_caps['noReset'] = True  # 记住之前的动作，不会清除之前的操作的一些缓存信息

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 打开APP，即跟server创建一个连接
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()  # 退出应用
        # self.driver.back()  # 返回到上一个页面

    @pytest.mark.parametrize('search, type, send', [('李四', '李四', '测试code'),('色橙1', '色橙1', '色橙1，你好'),('阿白', '阿白', '阿白，你好！')])
    def test_search(self, search, type, send):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()  # 进入通讯录
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gw1").click()  # 点击搜索按钮
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fl3").send_keys(search)  # 输入搜索词
        self.driver.find_element(MobileBy.XPATH, f"//*[@resource-id='com.tencent.wework:id/dhx']//*[@text='{type}']").click()  # 点击搜索出来的信息
        self.driver.find_element(MobileBy.XPATH, "//*[@text='发消息']").click()  # 点击发消息按钮
        el1 = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dxy")  # 定位输入框
        el1.click()  # 点击输入框
        el1.send_keys(send)  # 在该输入框输入需发送的内容
        # print(el1.text)  # 打印输入框中的内容
        actual_send = el1.text  # 把输入框中的实际内容复制给actual_send
        print(f"实际输入的内容：{actual_send}")
        print(f"期望输入的内容：{send}")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dxu").click()  # 点击发送按钮
        # assert_that(actual_send, equal_to(send))  # 第二种写法：断言实际的内容与输入的内容一致
        assert actual_send == send  # 第一种写法：断言实际的内容与输入的内容一致