import pytest
from test_appium.test_wechat.page.app import App

class TestDeleteMember:
    def setup(self):
        self.app = App()   # 实例化App类

    def teardown(self):
        pass

    @pytest.mark.parametrize('name', [
        ('小王2'),
        # ('小王3'),
        # ('小王4')
    ])
    def test_deletemember(self, name):
        # 这里最后一步点击确定后，是返回到AddressPage页的，这里保存这个页面
        addresspage = self.app.start().main().goto_address().delete_member(name).goto_edit_message().edit_member().delete_name()
        list = addresspage.search_member(name)  # 在这个页面调用search_member方法
        assert name not in list  # 断言被删除的成员，不在列表中，即成功删除