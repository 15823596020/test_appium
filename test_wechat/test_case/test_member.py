import pytest
import yaml

from test_appium.test_wechat.page.app import App

class TestMember:
    def setup(self):
        self.app = App()  # 实例化App类

    def teardown(self):
        self.app.stop()  # 调用退出应用方法

    # 读取测试数据文件
    def get_data():
        # ./表示当前路径  ..表示上级目录
        data = yaml.safe_load(open('./../datas/member.yaml', encoding='UTF-8'))  # 读取测试数据存放到data中
        # addmember_data = data['addmember']  # 读取添加成员的所有测试数据赋值给addmember_data
        # deletemember_data = data['deletemember']  # 读取删除成员的所有测试数据赋值给deletemember_data
        return data  # 返回data

    # @pytest.mark.parametrize('name, gender, phone, value', [
    #     ('小王2', '女', '17000001001', '添加成员'),
    #     # ('小王3', '男', '17000001002', '添加成员'),
    #     # ('小王4', '男', '17000001003', '添加成员')
    # ])
    @pytest.mark.parametrize('name, gender, phone, value', get_data()['addmember'])  # 参数化时，调用get_data方法，并传入添加成员的相关测试数据
    def test_addmember(self, name, gender, phone, value):
        # 这里最后一步点击保持后，是返回到AddMemberPage页的，这里保存这个页面
        addmemberpage = self.app.start().main().goto_address().add_member(value).manual_input_add().set_name(name).set_gender(gender).set_phonenum(phone).click_save()
        tip = addmemberpage.get_toast()  # 在这个页面调用获取toast的方法
        assert tip == "添加成功"


    # @pytest.mark.parametrize('name', [
    #     ('小王2'),
    #     # ('小王3'),
    #     # ('小王4')
    # ])
    @pytest.mark.parametrize('name', get_data()['deletemember'])   # 参数化时，调用get_data方法，并传入删除成员的相关测试数据
    def test_deletemember(self, name):
        # 这里最后一步点击确定后，是返回到AddressPage页的，这里保存这个页面
        addresspage = self.app.start().main().goto_address().delete_member(name).goto_edit_message().edit_member().delete_name()
        list = addresspage.searchs(name)  # 在这个页面调用查找元素列表方法searchs
        assert name not in list  # 断言被删除的成员，不在列表中，即成功删除