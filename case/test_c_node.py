# -*- coding: utf-8 -*-
import seldom
from seldom import Seldom, depend
from page.node_page import NodePage
from page.project_page import ProjectPage
from func.common_func import commonFunc

class NodeTest(seldom.TestCase):
    global page,ppage
    page = NodePage(Seldom.driver)
    ppage = ProjectPage(Seldom.driver)

    def start(self):
        """初始化"""
        page.open(commonFunc.baseUrl(self) + NodePage.node_url)
        self.max_window()
        self.wait(1)

    def down(self):
        """退出测试"""
        self.quit()

    @classmethod
    def setUpClass(cls):
        cls().start()

    def test01(self):
        """取消新增Node"""
        page.node_add.click()
        self.assertText('智能进化程度')
        page.project_dropdown.click()
        page.select_project.click()
        text = commonFunc.testText(self)
        page.node_name.input(text=text)
        page.cancel_add.click()
        self.wait(1)
        self.assertNotText(text)

    def test02(self):
        """新增Node"""
        page.node_add.click()
        self.assertText('智能进化程度')
        page.project_dropdown.click()
        page.select_project.click()
        global nname,pid
        nname = commonFunc.testText(self)
        page.node_name.input(text=nname)
        page.add_sure.click()
        self.wait(1)
        self.assertText(nname)
        pid = page.node_id.text[6:]

    def test03(self):
        """重置搜索"""
        text = commonFunc.testText(self)
        page.node_search_input.input(text=text)
        page.node_reset.click()
        self.wait(1)
        self.assertNotText(text)

    @depend("test02")
    def test04(self):
        """搜索Nodeid"""
        page.node_search_input.input(text=pid)
        page.node_search.click()
        self.wait(1)
        self.assertText(nname)

    @depend("test02")
    def test05(self):
        """搜索Node名称"""
        page.node_search_input.input(text=nname)
        page.node_search.click()
        self.wait(1)
        self.assertText(pid)

    @depend("test02")
    def test06(self):
        """搜索无结果"""
        page.node_search_input.input(text=nname+'invalid')
        page.node_search.click()
        self.wait(1)
        self.assertNotText(nname+'invalid')

    def test07(self):
        """前往第x页"""
        page.page_input.clear()
        page.page_input.input(text='2')
        page.node_id.click()
        self.wait(1)
        self.assertEqual(page.page_num.text,'2')

    @depend("test02")
    def test08(self):
        """下一页"""
        page.next_page.click()
        self.wait(1)
        self.assertNotText(nname)

    @depend("test02")
    def test09(self):
        """上一页"""
        page.last_page.click()
        self.wait(1)
        self.assertText(nname)

    def test10(self):
        """切换每页x条"""
        page.select_dropdown.click()
        self.wait(1)
        self.assertText('12条/页')
        page.select_list.click()
        self.wait(1)
        self.assertNotText('6条/页')

    @depend("test02")
    def test11(self):
        """查看项目下Node"""
        page.project_tab.click()
        self.assertText('项目列表')
        ppage.x_node.click()
        self.wait(1)
        self.assertText('Node 列表')
        self.assertText(nname)
