# -*- coding: utf-8 -*-
import seldom
from seldom import Seldom

from func.common_func import commonFunc
from page.project_page import ProjectPage

class testSSO(seldom.TestCase):
    def start(self):
        """初始化"""
        page = ProjectPage(Seldom.driver)
        page.open(commonFunc.baseUrl(self) + ProjectPage.project_url)
        self.max_window()
        self.wait(1)

    def down(self):
        """退出测试"""
        self.quit()

    @classmethod
    def setUpClass(cls):
        cls().start()

    def test01(self):
        """sso登录"""
        self.add_cookie({'name' : 'sso-t', 'value' : 'L7W6E4IA4LS6U3TYCIW3YHGUMJVB6PAUVVIXTZYSPPUPFXVAALE4XGSYTAFEZ2AD6WB6XZ37YPOTVQYRABV2BYYXA4T4ERJXDGLOGZQ','Domain' : '.rct.ai','Path' : '/'})
        self.refresh()
        self.assertText('管理后台')



