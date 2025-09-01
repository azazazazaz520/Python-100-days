#字典的定义
my_dict = {
    "q" : 123,
    "r" : 345
}              
#空字典
my_dict1 = {}
my_dict2 = dict()
#字典中重复的元素
my_dict3 = {"b" : 12 ,"b" : 133}
print(f"字典中的内容是:{my_dict3}")
#字典不能用下表索引，基于key获取value
print(f"q的值是:{my_dict['q']}")
#字典的嵌套
stu_score_dict = {
    "张三" : {
        "语文" : 80,
        "数学" : 70
    } ,
    "李四" : {
        "语文" : 86,
        "数学" : 74
    }
}
print(f"学生考试信息是：{stu_score_dict}")
print(f"李四的语文成绩是：{stu_score_dict['李四']['语文']}")
#新增字典元素
my_dict['t'] = 44
print(f'字典的元素为{my_dict}')

#更新字典元素
my_dict['q'] = 1456
print(f'q的元素被更改为{my_dict["q"]}')
#删除元素
value = my_dict.pop('q')
print(f'字典中的元素现在为{my_dict}')
#清空元素
my_dict.clear()
print(f"字典中的元素现在是{my_dict}")
#遍历字典
my_dict = {
    "q" : 123,
    "r" : 345
}   
keys = my_dict.keys()
print("字典中的元素value分别为：")
for key in keys:
    print(my_dict[key])
#直接对字典进行遍历
for key in my_dict:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{my_dict[key]}")
#统计字典的元素数量
num = len(my_dict)
print(f"字典的元素数量为:{num}")