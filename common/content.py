import re
# s='{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
# data={"mobilephone":"18800000000","pwd":"123456"}
#
# p="\$\{admin_user}"  #原本字符的写法
# p1="\$\{(.*?)}"      #元字符和限定符，（）代表组,?最多匹配一次
# m=re.search(p1,s)    #任意位置开始找，找到一个就返回match
# print(m)
# g1=m.group(1)           #取一个组的字符串
# print(g1)
# value=data[g1]
# print(value)
# s=re.sub(p1,value,s)

#s 是目标字符串
#d 是替换的内容
# 找到目标字符串里面的标识符KEY ，去d里面拿到替换的值
# 替换到s里面去 然后在返回
def replace(s,d):
        p="\$\{(.*?)}"
        print(d)
        while re.search(p,s):
                m=re.search(p,s)
                print(m)
                key=m.group(1)
                print("获取的key的值{}：".format(key))
                value=d[key]
                print("获取的value的值{}：".format(value))
                s=re.sub(p,value,s,count=1)

        return s
s='{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
data={"admin_user":"15873171553","admin_pwd":"123456"}
s=replace(s,data)
print(s)