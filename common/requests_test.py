import requests
from common.config import ReadConfig

import logging
import logging.handlers
from common import loggers
logger= loggers.get_log('login')  #注意模块调用模块中的方法，模块也可调用模块中的常量或类
logger.debug('获取日志类方法成功')

class Request:
    def __init__(self):
        self.session = requests.sessions.session()  #requests.sessions.Session`是一个建立会话的类
        self.value=ReadConfig().get('api', 'pre_url')  #读取配置文件的不同环境

    def request(self,method,url,data=None):
        url = self.value + url
        logger.info("地址是：{}".format(url))
        if data is not None and type(data)==str:
            logger.debug(data)
            data=eval(data)
        method=method.upper()

        if method=='GET':
            re=self.session.request(method,url,params=data)  #注意：get或post接收的数据类型必须是字典类型
        elif method=='POST':
            re=self.session.request(method, url, data=data)


        return re.text


if __name__ == '__main__':
    r =Request()
    data={"mobilephone":"13100000001",'pwd':123456}
    re=r.request("post","/member/login",data=data)
    print(re)