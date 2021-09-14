"""
发送测试结果邮件
"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common import readconfig
from common import consts
from common import log



class SendMail():

    def __init__(self):
        self.log = log.MyLog()

    def sendMail(self):
        msg = MIMEMultipart()
        # body = """
        # <h3>Hi，all</h3>
        # <p>本次接口自动化测试报告如下。</p>
        # """
        # mail_body = MIMEText(body, _subtype='html', _charset='utf-8')
        summary = consts.RESULT_LIST
        detail = consts.ERROR_DETAIL
        body2 = 'Hi，all\n本次接口自动化测试报告如下：\n   接口运行结果集：%s\n   错误结果出现位置：%s' % (summary, detail)
        mail_body2 = MIMEText(body2, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口自动化测试报告"+"_"+tm, 'utf-8')
        sender = readconfig.read_config('baseconfig', 'EMAIL', 'username')
        msg['From'] = sender
        receivers = readconfig.read_config('baseconfig', 'EMAIL', 'receiver')
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        # msg.attach(mail_body)

        msg.attach(mail_body2)

        smtpserver  =  readconfig.read_config('baseconfig', 'EMAIL', 'smtpserver')
        username = readconfig.read_config('baseconfig', 'EMAIL', 'username')
        password = readconfig.read_config('baseconfig', 'EMAIL', 'password')

        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(username, password)
            smtp.sendmail(sender, toclause, msg.as_string())
        except Exception as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")

        else:
            print("发送成功")
            self.log.info("邮件发送成功")
        finally:
            smtp.quit()
