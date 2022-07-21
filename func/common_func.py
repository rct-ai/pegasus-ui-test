import random

class commonFunc():

    def baseUrl(self):
        """测试环境"""
        baseUrl = 'https://pegasus-admin-test.rct.ai'
        return baseUrl

    def testText(self):
        """测试文案"""
        text = random.sample('abcdefghijklmnopqrstuvwxyz',6)
        return str(text)
