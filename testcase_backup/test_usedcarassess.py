# -*- coding: utf-8 -*-
import sys
sys.path.append('')
from common.httprequest import HttpRequest
import allure
from common import assertion

class TestUsedcarassess:
    @allure.feature('TestUsedcarassess')
    @allure.severity('blocker')
    def test_usedcarassess(self,usedcarassess):
        assertt = assertion.Assertion()
        self.case_name = usedcarassess[0]
        self.path = usedcarassess[1]
        self.method = usedcarassess[2]
        self.cookies = usedcarassess[3]
        self.query = usedcarassess[4]
        self.chcek_result = usedcarassess[5]
        result = HttpRequest().send_request(self.method, self.path, self.query,self.cookies)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        
        #下面自己补充断言或者其他验证数据的逻辑即可
        resvalue = float(result['result']['referenceprice'].split('-')[0])

        assertt.assert_moreorequal(self.chcek_result['referenceprice'], resvalue)