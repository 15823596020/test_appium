import pytest
from test_appium.test_wechat.page.app import App

class TestAddMember:
    def setup(self):
        self.app = App()  # 实例化App类

    def teardown(self):
        pass

    @pytest.mark.parametrize('name, gender, phone', [
        ('小王2', '女', '17000001001'),
        # ('小王3', '男', '17000001002'),
        # ('小王4', '男', '17000001003')
    ])
    def test_addmember(self, name, gender, phone):
        # 这里最后一步点击保持后，是返回到AddMemberPage页的，这里保存这个页面
        addmemberpage = self.app.start().main().goto_address().add_member().manual_input_add().set_name(name).set_gender(gender).set_phonenum(phone).click_save()
        tip = addmemberpage.get_toast()  # 在这个页面调用获取toast的方法
        assert tip == "添加成功"