import os

abs_path=os.path.abspath(__file__)  #当前文件的绝对路径
dir_path=os.path.dirname(abs_path)  #当前文件的上一级目录
get_path=os.getcwd()                #获取当前文件夹目录
dirn_name=os.path.dirname(os.getcwd())#根目录
data_path=os.path.join(dirn_name,'data/cases.xlsx')
conf_name =os.path.join(dirn_name,"conf")
conf_file=os.path.join(conf_name,"config.conf")
conf_global=os.path.join(conf_name,'global.conf')
conf_test=os.path.join(conf_name,'test.conf')
conf_test2=os.path.join(conf_name,'test2.conf')
log_name=os.path.join(dirn_name,'logsfir/python18.log')



# print(abs_path)
# print(dir_path)
# print(get_path)
# print(data_path)
# print(dirn_name)