import unittest
from common.do_excel import DoExcel
from common.requests_test import Request
from common import contains
from ddt import ddt,data
import warnings
from common.mysqlt import  MysqlUntil
import json
from common.get_atter import  Loan
@ddt
class LoanTest(unittest.TestCase):
                do_excel = DoExcel(contains.data_path, 'invest')
                conf_case = do_excel.get_conf("case", "row")
                re = do_excel.get_data(conf_case)  # 调用常量，需要先导常量所在文件包，在进行 文件名.常量，调用常量路径
                s = Loan()
                qq = Request()
                mysql = MysqlUntil()

                @classmethod
                def setUpClass(cls):

                    print("这是第一条用例开始仅执行一次")

                def setUp(self):
                    warnings.simplefilter('ignore',ResourceWarning)
                @data(*re)
                def test_loan(self,case):
                    case.data = self.s.replec(case.data)
                    qq = self.qq.request(case.method, case.url, case.data)

                    msg=json.loads(qq)
                    if msg["msg"]=='加标成功':
                        print(self.s.loan_member_id)
                        sql = "select id from future.loan where memberid={} order by createtime desc limit 1".format(self.s.loan_member_id)
                        self.result = self.mysql.fetch_one(sql)
                        setattr(Loan, 'loan_id',str(self.result[0]))

                    try:
                        self.assertEqual(case.expected,qq,'login_error')  #将返回结果和期望结果进行匹配
                        self.do_excel.write_data(case.case_id + 1, qq, 'PASS')
                        print("第{}条用例执行结果：PASS,测试数据{}".format(case.case_id,case.data))

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
    lt=LoanTest()
    lt.test_loan()