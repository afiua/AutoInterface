#	-*-	coding:	utf-8	-*
"""读取配置文件的内容
"""
import  os
import configparser

rootpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#获取项目所在的目录绝对路径

def read_config(file, section, name):
    #file需要读取配置的配置文件名称、section配置文件的节点名
    filename = file + '.ini'
    filepath = os.path.join(rootpath,'config', filename)
    cf = configparser.ConfigParser()
    cf.read(filepath, encoding='utf-8')
    return cf.get(section, name)



