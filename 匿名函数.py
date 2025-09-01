#函数作为参数传递
def test_func(compute):
    result = compute(1,2)
    print(f'compute参数的类型是:{type(compute)}')
    print(f'compute函数的计算结果是:{result}')
def compute(x,y):
    return x + y
test_func(compute)
#lambda匿名函数
test_func(lambda x , y:x + y)