''' 位置
    关键字
    缺省
    不定长
'''
def user_info(name,age,gender = "男"):
    print(f"姓名是:{name},年龄是:{age},性别是:{gender}")

#位置参数
user_info('小明','15','男')
#关键字参数
user_info(name = "小明", age = "15", gender = "男")
#缺省参数(设置默认值时参数必须统一放在最后)
user_info(name = "小天", age = "13")
#不定长参数
def user_info1(*args):    #位置不定长,args为形式参数作为元组存在
    print(f'args参数的类型是:{type(args)},内容是:{args}')
    
user_info1(1,1,3,'hello')


def user_info2(**kwargs):      #关键字不定长，kwargs作为字典存在
    print(f'args参数的类型是:{type(kwargs)},内容是:{kwargs}')
user_info2(name = '小王',age = '19',gender = '女')