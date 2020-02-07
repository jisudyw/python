import unittest
from common.do_excel import DoExcel
from common.requests_test import Request
from common import contains
from ddt import ddt,data
import warnings

import logging
import logging.handlers
from common import loggers
logger= loggers.get_log('login')  #注意模块调用模块中的方法，模块也可调用模块中的常量或类
logger.debug('获取日志类方法成功')
@ddt
class LoginTest(unittest.TestCase):
                do_excel = DoExcel(contains.data_path, 'login')
                conf_case = do_excel.get_conf("case", "row")
                re = do_excel.get_data(conf_case)  # 调用常量，需要先导常量所在文件包，在进行 文件名.常量，调用常量路径

                def setUp(self):
                    pass
                    logger.warn('Enable tracemalloc to get the object allocation traceback')
                    # warnings.simplefilter('ignore',ResourceWarning)
                @data(*re)
                def test_login(self,case):
                    qq= Request().request(case.method, case.url, case.data)
                    try:
                        self.assertEqual(case.expected,qq,'login_error')  #将返回结果和期望结果进行匹配
                        self.do_excel.write_data(case.case_id + 1, qq, 'PASS')
                        logger.info("第{}条用例执行结果：PASS".format(case.case_id))

                    except AssertionError as e:
                        self.do_excel.write_data(case.case_id + 1, qq, 'FAIL')
                        logger.info("第{}条用例执行结果：FAIL".format(case.case_id))
                        logger.error(e)
                def tearDown(self):
                    pass

if __name__ == '__main__':
    lt=LoginTest()
    lt.test_login()

#注意点：1.重复注册 2.url地址重复，可写在配置文件中 3.