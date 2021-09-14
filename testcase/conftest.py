import pytest
from common import get_casedate
import os

rootpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) #rootpath项目根目录
dirpath = os.path.join(rootpath,'params')  #dirpath测试用例数据存放的目录
casedata = get_casedate.Param()

#定义动态创建函数的语句
FUNC_TEMPLATE = """
@pytest.fixture(params={param})
def {func}(request):
    return request.param
"""
for root, dirs, files in os.walk(dirpath):
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
    for filename in files:
        casename = filename.split('.')[0]  #测试用例数据文件去掉后面的文件名
        caselistdata = casedata.get_casedata(filename)

        #以casename为函数名，动态创建函数，
        exec(FUNC_TEMPLATE.format(param=caselistdata,func=casename))
