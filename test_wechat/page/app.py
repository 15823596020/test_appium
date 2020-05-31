from appium import webdriver
from test_appium.test_wechat.page.basepage import BasePage
from test_appium.test_wechat.page.main_page import MainPage

class App(BasePage):  # 继承BasePage类
    # 启动app
    def start(self):
        if self._driver == None:  # 如果这个self._driver为None，就初始化一个driver
            desired_caps = {}
            desired_caps['platformName'] = 'Android'  # 平台
            desired_caps['platformVersion'] = '6.0'  # 平台版本
            desired_caps['deviceName'] = '127.0.0.1:7555'  # 设备名字
            desired_caps['appPackage'] = 'com.tencent.wework'  # 需要打开的包名
            desired_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'  # 打开APP的第一个activity
            desired_caps['noReset'] = True  # 记住之前的动作，不会清除之前的操作的一些缓存信息
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 打开APP，即跟server创建一个连接
        else:
            self._driver.launch_app()  # 否则就复用这个driver，并且启用app
        self._driver.implicitly_wait(5)  # 隐式等待
        return self  # 初始化_driver后，返回自己

    # 重启app
    def restart(self):
        pass

    # 停止app
    def stop(self):
        self._driver.quit()  # 退出应用

    # 进入主页
    def main(self) -> MainPage:  # ->MainPage表示一个类型提示
        return MainPage(self._driver)  # 实例化MainPage，进入主页
