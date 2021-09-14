# -*- coding: utf-8 -*-
import sys
sys.path.append('')
from common.httprequest import HttpRequest
import allure
from common import assertion
from datetime import datetime
from common import consts

class TestGetcallentrance:
    @allure.feature('TestGetcallentrance')
    @allure.severity('blocker')
    def test_GetCallEntrance(self,GetCallEntrance):
        assertt = assertion.Assertion()
        self.case_name = GetCallEntrance[0]
        self.path = GetCallEntrance[1]
        self.method = GetCallEntrance[2]
        self.cookies = GetCallEntrance[3]
        self.query = GetCallEntrance[4]
        self.chcek_result = GetCallEntrance[5]
        result = HttpRequest().send_request(self.method, self.path, self.query,self.cookies)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        
        #下面自己补充断言或者其他验证数据的逻辑即可
        nowhour=datetime.now().hour
        if nowhour>=20 or nowhour<8:
            assertt.assert_common(0, result['result']['isshow'])
            assertt.assert_common(0, result['result']['iswindow_show'])
        elif self.query['producttype'] == 1:
            assertt.assert_common(1, result['result']['isshow'])
            assertt.assert_common(1, result['result']['iswindow_show'])
            if(self.query['cid'] in [510100,110100,310100]):
                assertt.assert_common(1, result['result']['isim_show'])
                assertt.assert_common(1, result['result']['isimwindow_show'])
            else:
                assertt.assert_common(0, result['result']['isim_show'])
                assertt.assert_common(0, result['result']['isimwindow_show'])

        elif self.query['producttype'] == 2:
            assertt.assert_common(1, result['result']['isshow'])
            assertt.assert_common(0, result['result']['iswindow_show'])
            if (self.query['cid'] in [510100, 110100, 310100]):
                assertt.assert_common(1, result['result']['isim_show'])
                assertt.assert_common(1, result['result']['isimwindow_show'])
            else:
                assertt.assert_common(0, result['result']['isim_show'])
                assertt.assert_common(0, result['result']['isimwindow_show'])
        elif self.query['producttype'] == 3:
            assertt.assert_common(0, result['result']['isshow'])
            assertt.assert_common(1, result['result']['iswindow_show'])
            assertt.assert_common(1, result['result']['isim_show'])
            assertt.assert_common(1, result['result']['isimwindow_show'])
        elif self.query['producttype'] == 4:
            assertt.assert_common(1, result['result']['isshow'])
            assertt.assert_common(0, result['result']['iswindow_show'])
            assertt.assert_common(0, result['result']['isim_show'])
            assertt.assert_common(0, result['result']['isimwindow_show'])

        consts.RESULT_LIST.append('T')
