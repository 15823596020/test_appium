"""
课后作业
PO模式实现 企业微信添加联系人、删除联系人功能
封装 find 处理异常、弹框
实现参数化
注意点
删除的时候需要验证联系不展示在联系人列表
"""
from time import sleep

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

    @pytest.mark.parametrize('name, gender, phone', [
        ('小王2', '女', '17000001001'),
        # ('小王3', '男', '17000001002'),
        # ('小王4', '男', '17000001003')
    ])
    def test_add(self, name, gender, phone):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()  # 点击通讯录，进入通讯录页面
        # 滚动查找添加成员，并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手动输入')]").click()  # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys(name)  # 定位姓名输入框，并输入姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()  # 点击性别
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{gender}']").click()  # 点击选择性别
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机') and contains(@class,'TextView')]/..//*[@text='手机号']").send_keys(phone)  # 定位手机号输入框，并输入手机号
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()  # 点击保存按钮

        el2 = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]')  # 定位toast
        # print(el2.text)
        assert el2.text == "添加成功"   # 断言toast的文本是添加成功，即表示添加成员成功

    @pytest.mark.parametrize('name', [
        ('小王2'),
        # ('小王3'),
        # ('小王4')
    ])
    def test_delete(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()  # 点击通讯录，进入通讯录页面
        # 滚动查找需删除的成员，并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//*[@resource-id='com.tencent.wework:id/gvr']").click()  # 点击右上角的三个点
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()  # 点击编辑成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()  # 点击删除成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()  # 点击确定
        # 再次滚动查找被删除的成员
        el1_list = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));')
        # print(len(el1_list))  # 打印el1_list列表的长度
        # assert len(el1_list) == 0  # 断言这个长度为0，就表示被删除的成员已不在列表中，即成功删除
        assert name not in el1_list  # 断言被删除的成员，不在列表中，即成功删除