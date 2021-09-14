# -*- coding: utf-8 -*-
"""根据目录params下的测试数据文件去自动创建测试用例文件
比如说params下有文件a.xlsx或者a.yaml,但是testcase和testcase_backup文件夹下没有对应的test_a.py的时候，
执行此工具则会自动以下面变量CREAT_CASEEFILE_STR为模板创建test_a.py
"""
import os

rootpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) #rootpath项目根目录
casedatepath = os.path.join(rootpath,'params')  #dirpath测试用例数据存放的目录
testcasedir = os.path.join(rootpath,'testcase') #dirpath测试用例文件存放的目录
testcase_backupdir =os.path.join(rootpath,'testcase_backup') #dirpath测试用例文件存放的目录
testcaselist=[]  #用于储存现有测试用例文件的列表

#创建测试用例文件用的模板
CREAT_CASEEFILE_STR ="""# -*- coding: utf-8 -*-
import sys
sys.path.append('')
from common.httprequest import HttpRequest
import allure
from common import  consts
from common import assertion

class {classname}:
    @allure.feature('{classname}')
    @allure.severity('blocker')
    def {funname}(self,{fname}):
        assertt = assertion.Assertion()
        self.case_name = {fname}[0]
        self.path = {fname}[1]
        self.method = {fname}[2]
        self.cookies = {fname}[3]
        self.query = {fname}[4]
        self.chcek_result = {fname}[5]
        result = HttpRequest().send_request(self.method, self.path, self.query,self.cookies)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        
        #下面自己补充断言或者其他验证数据的逻辑即可
"""
for root, dirs ,files in os.walk(testcasedir):
    for file in files:
        testcaselist.append(file)

for root, dirs ,files in os.walk(testcase_backupdir):
    for file in files:
        testcaselist.append(file)

for root, dirs, files in os.walk(casedatepath):
    for file in files:
        filename = 'test_'+file.split('.')[0]+'.py'
        if filename not in testcaselist:
            fname= file.split('.')[0]
            classname = 'Test' + fname.capitalize()
            funname = 'test_' + fname
            file_object = open(os.path.join(testcasedir, filename), 'w' ,encoding='utf8')
            file_object.writelines(CREAT_CASEEFILE_STR.format(classname=classname ,funname=funname ,fname=fname))
            file_object.close()
            print(CREAT_CASEEFILE_STR.format(classname=classname ,funname=funname ,fname=fname))
