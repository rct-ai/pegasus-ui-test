# -*- coding: utf-8 -*-
from poium import Page, Element


class NodePage(Page):
    """Node管理页面"""
    #url
    node_url = '/node/list'

    #搜索框
    node_search_input = Element(xpath='//*[@class="el-input el-input--small"]/input')

    #查询按钮
    node_search = Element(xpath='//button[@class="el-button el-button--primary el-button--small"]')

    #重置按钮
    node_reset = Element(xpath='//button[@class="el-button el-button--default el-button--small"]')

    #新增Node
    node_add = Element(xpath='//*[@class="route-header__right text-xs text-gray-500 flex items-center"]/button')

    #项目拉下框
    project_dropdown = Element(xpath='//*[@class="el-form-item__content"]/div/div/div/span/span')

    #选择项目
    select_project = Element(xpath='//*[@id="el-popper-3485"]/div[1]/div/div[1]/ul/li[1]')

    #Node名称输入框
    node_name = Element(xpath='//*[@class="el-input el-input--medium"]/input')

    #确定新增
    next_step = Element(xpath='//*[@class="el-form-item__content"]/button[2]')

    #取消新增
    cancel_add =  Element(xpath='//*[@class="el-form-item__content"]/button[1]')

    #页码输入框
    page_input = Element(xpath='//*[@class="el-pagination"]/span/div/input')

    #当前页码
    page_num = Element(xpath='//ul[@class="el-pager"]/li[2]')

    #上一页
    last_page = Element(xpath='//button[@class="btn-prev"]')

    #下一页
    next_page = Element(xpath='//button[@class="btn-next"]')

    #每页x条下拉
    select_dropdown = Element(xpath='//*[@class="el-pagination__sizes"]/div/div/div/span')

    #每页x条
    select_list = Element(xpath='//*[@aria-hidden="false"]/div/div/div/ul/li[2]/span')

    #Nodeid
    node_id = Element(xpath='//div[@class="el-card is-hover-shadow list-item border mb-4"]/div/div/div[2]')

    #项目管理tab
    project_tab = Element(xpath='//ul[@class="el-menu"]/li[1]')