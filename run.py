import pytest
from common import shell
from common import consts
import os
from common import email


if __name__ == '__main__':

    #shell = shell.Shell()
    ss=os.path.abspath(os.path.dirname(__file__))

    xml_report_path = os.path.join(ss,'report','xml')
    html_report_path = os.path.join(ss,'report','html')
    #xml_report_path = xml_report_path.replace('\\','/')
    #html_report_path = html_report_path.replace('\\','/')

    args = ['./testcase','-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)

    cmd = 'allure generate -c %s -o  %s' % (xml_report_path, html_report_path)
    # cmd='calc'
    try:
        shell.Shell.exexute(cmd)
    except Exception:
        raise

    # try:
    #     mail = email.SendMail()
    #     mail.sendMail()
    # except Exception as e:
    #     #log.error('发送邮件失败，请检查邮件配置')
    #     raise


