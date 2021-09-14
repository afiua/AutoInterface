#	-*-	coding:	utf-8	-*
import os
from xlrd import open_workbook
from common import readconfig
import yaml
class Param():
    def get_casedatepath(self, filename):
        #获取测试用例数据的路径
        rootpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        casedatepath = os.path.join(rootpath, 'params', filename)
        return casedatepath


    def get_casedata(self, filename, sheetname='Sheet1'):
        """读取filename中的数据，并处理成以下格式
        [list1,list2,list3.....]list123表示一条用例
        lise1本身又是一个list,包含用例名称、url、请求方式（post or get）、cookie(字典)、请求参数（字典）、期望结果（字典）共6项基础数据
        此处需要注意的是需要excel的文件名和配置文件interfaceconfig.ini中的section名称一致
        """
        filepath = self.get_casedatepath(filename)
        if  filename.split('.')[-1] == 'xlsx':
            casedata = []

            excel = open_workbook(filepath)
            sheetdata = excel.sheet_by_name(sheetname)
            rows = sheetdata.nrows
            cols = sheetdata.ncols

            for i in range(4, cols):
                xls_cols = []
                param = {}
                xls_cookie = {}
                xls_result = {}

                xls_cols.append(sheetdata.cell_value(0, i))  # 用例名称
                xls_cols.append(readconfig.read_config('interfaceconfig', filename.split('.')[0], 'httpurl'))  # URL
                xls_cols.append(readconfig.read_config('interfaceconfig', filename.split('.')[0], 'method'))  # 请求方式post or get
                for j in range(1, rows):
                    cell0 = str(sheetdata.cell_value(j, 0))

                    ctype = sheetdata.cell(j, i).ctype  # 表格的数据类型
                    # ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
                    cell = sheetdata.cell_value(j, i)

                    if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
                        cell = int(cell)
                    if cell != '' and not cell0.startswith('result') and not cell0.startswith('cookie'):
                        param[cell0] = cell
                    if cell0.startswith('result'):
                        xls_result[cell0.split('*')[-1]] = cell
                    if cell0.startswith('cookie'):
                        xls_cookie[cell0.split('*')[-1]] = cell

                xls_cols.append(xls_cookie)  # cookie
                xls_cols.append(param)  # 请求参数
                xls_cols.append(xls_result)  # 期望结果
                casedata.append(xls_cols)

            return casedata
        elif filename.split('.')[-1] == 'yaml':
            casedata = []

            with open(filepath, 'r', encoding='utf-8') as f:
                yamlcontent = yaml.safe_load(f)

            for para_result_cookie in yamlcontent['ParamAndRes']:
                yaml_cols = []
                Nonedict = {}
                yaml_cols.append(para_result_cookie['casename'])
                yaml_cols.append(readconfig.read_config('interfaceconfig', filename.split('.')[0], 'httpurl'))  # URL
                yaml_cols.append(
                    readconfig.read_config('interfaceconfig', filename.split('.')[0], 'method'))  # 请求方式post or get
                try:
                    yaml_cols.append(para_result_cookie['cookies'])
                except:
                    yaml_cols.append(Nonedict)

                try:
                    yaml_cols.append(para_result_cookie['parameter'])
                except:
                    yaml_cols.append(Nonedict)

                try:
                    yaml_cols.append(para_result_cookie['exceptresult'])
                except:
                    yaml_cols.append(Nonedict)

                casedata.append(yaml_cols)

            return casedata

if __name__ == '__main__':
    s = Param()
    b= s.get_casedata('newclue.xlsx')
    #b = s.get_casedata('usedcarassess.yaml')
    print(b)

