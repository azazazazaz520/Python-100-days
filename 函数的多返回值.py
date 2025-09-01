#函数的多返回值
def test1_return():
    return 1,"hello",{
        "y" : 888,
        "s" : 213
    }
x,y,z = test1_return()
print(x)
print(y)
print(z)