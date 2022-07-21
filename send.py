# -*- coding: utf-8 -*-
import os
import requests
import json

def testReport():
    path = os.getcwd() + '/reports'
    name = os.listdir(path)
    print(type(name),name)
    fileName = list(filter(lambda a:a.find("result") >= 0,name))
    print(fileName)
    #return ''.join(fileName)

    p = {
    "msg_type": "interactive",
    "card": {
        "config": {
                "wide_screen_mode": True,
                "enable_forward": True
        },
        "elements": [{
                "actions": [{
                        "tag": "button",
                        "text": {
                                "content": "点击查看测试报告 🔍",
                                "tag": "lark_md"
                        },
                        "url": "https://jenkins.dev-metaverse.fun/view/test/job/test-pegasus-ui-automation/HTML_20Report/",
                        "type": "default",
                        "value": {}
                }],
                "tag": "action"
        }],
        "header": {
                "title": {
                        "content": "🔔 Pegasus管理后台UI自动化回归测试",
                        "tag": "plain_text"
                }
        }
    }
}
    toFS = requests.post('https://open.feishu.cn/open-apis/bot/v2/hook/1eba2ae5-9ad4-4acc-b3fe-3b53ce9f97a7',json.dumps(p))
    print(toFS.status_code, toFS.json())
    return toFS

if __name__ == '__main__':
    testReport()
