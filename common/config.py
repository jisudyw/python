import configparser
from common import contains


class ReadConfig:  # 读取配置文件
    def __init__(self):

        self.config = configparser.ConfigParser()
        self.config.read(contains.conf_global,encoding='utf-8')   #打开配置文件
        open=self.config.getboolean('switch', 'open')             #获取配置文件的value值，并且转化为boolean类型
        if open==True:   #如果配置文件global.conf中的open==True,则选择test.conf中的环境，否则选择test2.conf中的环境
            self.config.read(contains.conf_test, encoding='utf-8')
        else:
            self.config.read(contains.conf_test2, encoding='utf-8')
    def get(self, section, option):
         return self.config.get(section, option)



ReadConfig().get('api','pre_url')

