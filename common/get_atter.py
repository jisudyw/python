from common.config import ReadConfig
import re

class Loan:
    config=ReadConfig()
    admin_user =config.get('data','admin_user')
    admin_pwd =config.get('data','admin_pwd')
    loan_member_id =config.get('data','loan_member_id')
    normal_user =config.get('data','normal_user')
    normal_pwd=config.get('data','normal_pwd')
    normal_member_id =config.get('data','normal_member_id')



    def replec(self,s):
        p="\${(.*?)}"
        while re.search(p,s):
            m=re.search(p,s)
            key=m.group(1)
            value=getattr(Loan,key)
            s=re.sub(p,value,s,count=1)
        return s




if __name__ == '__main__':
    s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
    k=Loan()
    m=k.replec(s)
    print(m)
