import json

# people = '{"name":"张先生","age":null,"sex":"false"}'
# json_name=json.loads(people)     #序列化  json格式的字符串类型转化为字典格式，json.loads()

# str_name=json.dumps(json_name)   #反序列化 字典格式转化为json格式的字符串类型

o =open("jsons.py", encoding="utf-8")#首先打开文件，然后用户json.load加载文件,用py结尾的文件不支持null，有null的json数据不要用py文件
mm=json.load(o)
print(mm)
