"""
断言封装，初步完成=，>=,<=,>,<等5中断言
"""
from common import  log
from common import consts
import traceback

#日志
logger = log.MyLog().get_logger()

class Assertion():

    def assert_common(self, expectmsg, resultmsg):
        #验证是否相等
        try:
            assert expectmsg == resultmsg
            return True
        except:
            logger.info('expectmsg:{} 不等于resultmsg:{}'.format(expectmsg, resultmsg))
            consts.RESULT_LIST.append('F')
            #traceback.extract_stack()[35]可以获取调用该函数是从那个测试用例文件调用的
            consts.ERROR_DETAIL.append(traceback.extract_stack()[35])
            logger.info('error on:{}'.format(traceback.extract_stack()[35]))
            raise


    def assert_lessorequal(self, expectmsg, resultmsg):
        # 验证期望值是否小于等于结果
        try:
            assert expectmsg <= resultmsg
            return True
        except:
            logger.info('expectmsg:{} 不小于等于resultmsg:{}'.format(expectmsg, resultmsg))
            consts.RESULT_LIST.append('F')
            # traceback.extract_stack()[35]可以获取调用该函数是从那个测试用例文件调用的
            consts.ERROR_DETAIL.append(traceback.extract_stack()[35])
            logger.info('error on:{}'.format(traceback.extract_stack()[35]))
            raise

    def assert_less(self, expectmsg, resultmsg):
        # 验证期望值是否小于结果
        try:
            assert expectmsg < resultmsg
            return True
        except:
            logger.info('expectmsg:{} 不小于resultmsg:{}'.format(expectmsg, resultmsg))
            consts.RESULT_LIST.append('F')
            # traceback.extract_stack()[35]可以获取调用该函数是从那个测试用例文件调用的
            consts.ERROR_DETAIL.append(traceback.extract_stack()[35])
            logger.info('error on:{}'.format(traceback.extract_stack()[35]))
            raise

    def assert_moreorequal(self, expectmsg, resultmsg):
        # 验证期望值是否大于等于结果
        try:
            assert expectmsg >= resultmsg
            return True
        except:
            logger.info('expectmsg:{} 不大于等于resultmsg:{}'.format(expectmsg, resultmsg))
            consts.RESULT_LIST.append('F')
            # traceback.extract_stack()[35]可以获取调用该函数是从那个测试用例文件调用的
            consts.ERROR_DETAIL.append(traceback.extract_stack()[35])
            logger.info('error on:{}'.format(traceback.extract_stack()[35]))
            raise

    def assert_more(self, expectmsg, resultmsg):
        # 验证期望值是大于结果
        try:
            assert expectmsg > resultmsg
            return True
        except:
            logger.info('expectmsg:{} 不大于resultmsg:{}'.format(expectmsg, resultmsg))
            consts.RESULT_LIST.append('F')
            # traceback.extract_stack()[35]可以获取调用该函数是从那个测试用例文件调用的
            consts.ERROR_DETAIL.append(traceback.extract_stack()[35])
            logger.info('error on:{}'.format(traceback.extract_stack()[35]))
            raise

if __name__ == '__main__':
    logger.info("222")