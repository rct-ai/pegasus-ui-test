# -*- coding: utf-8 -*-
import seldom
from seldom import Seldom, depend
from page.project_page import ProjectPage
from func.common_func import commonFunc

class ProjectTest(seldom.TestCase):
    global page
    page = ProjectPage(Seldom.driver)

    def start(self):
        """初始化"""
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
        """取消新增项目"""
        page.project_add.click()
        self.assertText('项目描述')
        text = commonFunc.testText(self)
        page.project_name.input(text=text)
        page.cancel_add.click()
        self.wait(1)
        self.assertNotText(text)

    def test02(self):
        """新增项目"""
        page.project_add.click()
        self.assertText('项目描述')
        global pname,pid
        pname = commonFunc.testText(self)
        page.project_name.input(text=pname)
        page.add_sure.click()
        self.wait(1)
        self.assertText(pname)
        pid = page.project_id.text[6:]

    def test03(self):
        """重置搜索"""
        text = commonFunc.testText(self)
        page.project_search_input.input(text=text)
        page.project_reset.click()
        self.wait(1)
        self.assertNotText(text)

    @depend("test02")
    def test04(self):
        """搜索项目id"""
        page.project_search_input.input(text=pid)
        page.project_search.click()
        self.wait(1)
        self.assertText(pname)

    @depend("test02")
    def test05(self):
        """搜索项目名称"""
        page.project_search_input.input(text=pname)
        page.project_search.click()
        self.wait(1)
        self.assertText(pid)

    def test06(self):
        """搜索无结果"""
        page.project_search_input.input(text=pname+'invalid')
        page.project_search.click()
        self.wait(1)
        self.assertNotText(pname+'invalid')

    def test07(self):
        """前往第x页"""
        page.page_input.clear()
        page.page_input.input(text='2')
        page.project_id.click()
        self.wait(1)
        self.assertEqual(page.page_num.text,'2')

    @depend("test02")
    def test08(self):
        """下一页"""
        page.next_page.click()
        self.wait(1)
        self.assertNotText(pname)

    @depend("test02")
    def test09(self):
        """上一页"""
        page.last_page.click()
        self.wait(1)
        self.assertText(pname)

    def test10(self):
        """切换每页x条"""
        page.select_dropdown.click()
        self.wait(1)
        self.assertText('12条/页')
        page.select_list.click()
        self.wait(1)
        self.assertNotText('6条/页')