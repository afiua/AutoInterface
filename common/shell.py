"""
封装执行shell命令
"""
import subprocess

class Shell():
    @staticmethod
    def exexute(cmd):
        res,err = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        r = res.decode("utf-8")
        e = err.decode("gbk")
        if e != '':
            print(e)
        else:
            print(r)

        return r
