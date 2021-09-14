# -*- coding: utf-8 -*-
import sys
sys.path.append('')
from common.httprequest import HttpRequest
import allure
from common import assertion

class TestNewclue:
    @allure.feature('TestNewclue')
    @allure.severity('blocker')
    def test_newclue(self,newclue):
        assertt = assertion.Assertion()
        self.case_name = newclue[0]
        self.path = newclue[1]
        self.method = newclue[2]
        self.cookies = newclue[3]
        self.query = newclue[4]
        self.chcek_result = newclue[5]
        result = HttpRequest().send_request(self.method, self.path, self.query,self.cookies)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        
        #下面自己补充断言或者其他验证数据的逻辑即可
