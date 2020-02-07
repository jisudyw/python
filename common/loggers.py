import logging
import logging.handlers
from common import contains
from common.config import ReadConfig
config=ReadConfig()


def get_log(logger_name):
        logger_level = config.get('log', 'logger_level')
        rfh_level = config.get('log', 'rfh_level')
        fmt = config.get('log', 'format')

        logger=logging.getLogger(logger_name)  #创建日志收集器
        logger.setLevel(logger_level)    #日志收集器设置级别


        format=logging.Formatter(fmt)  #注意：%分号是特殊字符，放在配置文件中需要进行转义为%%

        rfh_name=logging.handlers.RotatingFileHandler(contains.log_name,maxBytes=20*1024*1024, backupCount=10,)  #给日志设置输出渠道
        rfh_name.setLevel(rfh_level)         #给输出渠道设置级别
        rfh_name.setFormatter(format)
        logger.addHandler(rfh_name)        #日志收集器和输出渠道进行对接

        return logger



if __name__ == '__main__':
 logger=get_log('python33')

 logger.error('这是什么贵')
 # logger.removeHandler(rfh_name)



