# -*- coding: utf-8 -*-
import sys
sys.path.append('')
from common.httprequest import HttpRequest
import allure
from common import assertion

class TestGetxnumber:
    @allure.feature('TestGetxnumber')
    @allure.severity('blocker')
    def test_getxnumber(self,getxnumber):
        assertt = assertion.Assertion()
        self.case_name = getxnumber[0]
        self.path = getxnumber[1]
        self.method = getxnumber[2]
        self.cookies = getxnumber[3]
        self.query = getxnumber[4]
        self.chcek_result = getxnumber[5]
        result = HttpRequest().send_request(self.method, self.path, self.query,self.cookies)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        
        #下面自己补充断言或者其他验证数据的逻辑即可
        assertt.assert_common(str(self.chcek_result['xnumber']), result['result']['xnumber'])
