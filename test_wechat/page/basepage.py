import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

class BasePage:
    # 定义一个私有变量_black_list黑名单，把弹框都添加到黑名单中
    _black_list = [
        (MobileBy.XPATH, "//*[@text='下次再说']"),
        (MobileBy.XPATH, "//*[@text='确定']")
    ]
    _error_num = 0  # 弹窗次数
    _max_error_num = 3  # 设定最大的循环次数

    # 封装driver
    def __init__(self, driver: WebDriver = None):  # driver默认值为None
        self._driver = driver

    # 封装find方法，捕获异常，处理弹框
    def find(self, locator, value):
        # return self._driver.find_element(locator, value)  # 我的写法
        try:
            # 没有弹框，正常的处理流程
            if isinstance(locator, tuple):  # 判断类型，如果locator是一个元组，就需要解元组
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)  # 否则就直接传入两个值
            self._error_num = 0  # 将_error_num置零
            return element  # 返回element

        except Exception as e:  # 自定义一个异常，重命名为a，最终会抛出一个NoSuchElementException的异常信息
            if self._error_num > self._max_error_num:  # 如果弹窗的内容在黑名单中查找了3次，都没有找到，就直接抛出异常
                raise e
            self._error_num += 1  # 查找的次数加1

            for ele in self._black_list:  # 遍历黑名单
                ellist = self._driver.find_elements(*ele)  # 把找到的结果存放到ellist中,ele是元组，所以需要解元组
                if len(ellist) > 0:  # 如果大于0就表示找到了，即如果弹框存在于黑名单中
                    ellist[0].click()  # 就取出第一个元组进行点击
                    return self.find(locator, value)  # 继续调用find方法，继续查找
            raise e  # 抛出异常

    # 封装finds方法，查找多个元素
    def finds(self, locator, value):
        return self._driver.find_elements(locator, value)