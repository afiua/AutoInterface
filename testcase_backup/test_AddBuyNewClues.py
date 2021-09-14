# -*- coding: utf-8 -*-
import sys
sys.path.append('')
from common.httprequest import HttpRequest
import allure
from common import assertion
from common import  consts

class TestAddbuynewclues:
    @allure.feature('TestAddbuynewclues')
    @allure.severity('blocker')
    def test_AddBuyNewClues(self,AddBuyNewClues):
        assertt = assertion.Assertion()
        self.case_name = AddBuyNewClues[0]
        self.path = AddBuyNewClues[1]
        self.method = AddBuyNewClues[2]
        self.cookies = AddBuyNewClues[3]
        self.query = AddBuyNewClues[4]
        self.chcek_result = AddBuyNewClues[5]
        result = HttpRequest().send_request(self.method, self.path, self.query,self.cookies)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        
        #下面自己补充断言或者其他验证数据的逻辑即可
        consts.RESULT_LIST.append('T')