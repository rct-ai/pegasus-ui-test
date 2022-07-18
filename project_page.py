# -*- coding: utf-8 -*-
from poium import Page, Element


class ProjectPage(Page):
    """项目管理页面"""
    #url
    project_url = '/application/list'

    #搜索框
    project_search_input = Element(xpath='//*[@class="list__search flex items-center"]/div/input')

    #查询按钮
    project_search = Element(xpath='//*[@class="list__search flex items-center"]/button[1]')

    #重置按钮
    project_reset = Element(xpath='//*[@class="list__search flex items-center"]/button[2]')

    #新增项目
    project_add = Element(xpath='//*[@class="route-header__right text-xs text-gray-500 flex items-center"]/button')

    #项目名称输入框
    project_name = Element(xpath='//*[@class="el-form-item__content"]/div/input')

    #确定新增
    add_sure = Element(xpath='//*[@class="el-form-item"]/div/button[2]')

    #取消新增
    cancel_add =  Element(xpath='//*[@class="el-form-item"]/div/button[1]')

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

    #项目id
    project_id = Element(xpath='//div[@class="el-card is-hover-shadow list-item border mb-4"]/div/div/div[2]')