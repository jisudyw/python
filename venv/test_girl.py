#静态方法：必须先创建对象，才能用对象获取属性值 和调用方法
#动态方法：反射，不用创建对象，可直接获取属性值和调用方法，并可同时更改属性值和方法


class Girls:

    def __init__(self,name,age):
        self.name=name
        self.age=age


    def girl(self):
         print('这是一个女孩')


if __name__ == '__main__':
    m=Girls('mongo','18')
    getattr(m,'name')           #通过对象获取对象属性值，或通过类获取类属性值
    setattr(m,'sex','女')       #通过对象修改设置对象属性，或通过类修改设置类属性
    print(getattr(m,'sex'))     #

    setattr(Girls,'hobby','喜欢游泳')
    print(getattr(Girls,'hobby'))

    hasattr(Girls,'hobby')  # 判断 Girls这个类是否有 'hobby' 这个属性

    delattr(Girls,'hobby')  #删除 Girls这个类的'hobby'属性
