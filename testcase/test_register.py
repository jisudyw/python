import unittest
from common.do_excel import DoExcel
from common.requests_test import Request
from common import contains
from ddt import ddt,data
import warnings
from common.mysqlt import MysqlUntil

@ddt
class RegisterTest(unittest.TestCase):
                do_excel = DoExcel(contains.data_path, 'register')
                conf_case = do_excel.get_conf("case", "row")
                re = do_excel.get_data(conf_case)  # 调用常量，需要先导常量所在文件包，在进行 文件名.常量，调用常量路径
                mysql = MysqlUntil()              #连接数据库
                @classmethod
                def setUpClass(cls):
                    sql = "select max(mobilephone) from future.member where mobilephone like '131%'"
                    cls.result=cls.mysql.fetch_one(sql)
                    print("这是第一条用例开始仅执行一次")
                def setUp(self):
                    warnings.simplefilter('ignore',ResourceWarning)
                # @unittest.skip  #遇到skip相对应的方法就不执行
                @data(*re)
                def test_register(self,case):
                    import json
                    data_dict=json.loads(case.data)
                    mobile=data_dict['mobilephone']
                    if mobile=="${register_mobile}":  #参数化注册手机号码
                        print(self.result[0])
                        data_dict['mobilephone']=int(self.result[0])+1
                        print(data_dict)

                    qq=Request().request(case.method, case.url, data_dict)
                    try:
                        self.assertEqual(case.expected,qq,'注册失败')  #将返回结果和期望结果进行匹配
                        self.do_excel.write_data(case.case_id + 1, qq, 'PASS')
                        print("第{}条用例执行结果：PASS".format(case.case_id))
                    except AssertionError as e:
                        self.do_excel.write_data(case.case_id + 1, qq, 'FAIL')
                        print("第{}条用例执行结果：FAIL".format(case.case_id))
                        raise e
                def tearDown(self):
                    pass

                @classmethod
                def tearDownClass(cls):
                    cls.mysql.close_mysql()
                    print('这是所有用例执行完毕仅执行的一条语句')

if __name__ == '__main__':
    lt=RegisterTest()
    lt.test_register()