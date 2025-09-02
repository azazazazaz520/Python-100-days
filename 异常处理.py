'''
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
    '''
import os
print("当前工作目录:", os.getcwd())
try:
    f = open('./log.txt', 'r', encoding='UTF-8')
    print("文件存在，成功打开")
    f.close()   # 记得关闭文件
except:
    print('file did not exist')
    f = open('./log.txt', 'w', encoding='UTF-8')
    f.write('new')
    f.close()   # 记得关闭文件
    print("文件已创建并写入'new'")
#捕获指定异常
try:
    print(name)
except NameError as e:
    print('出现变量未定义的异常')
    print(e)
#捕获多个异常
try:
    #print(name)
    1 / 0
except (NameError,ZeroDivisionError) as e:
    print(e)


#捕获所有的异常
try:
    #print(name)
    print('a')
except Exception as e:
    print(e)

else:
    print('没有异常')
finally:
    #有无异常都会执行
    print('end')
