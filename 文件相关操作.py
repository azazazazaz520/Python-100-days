'''
文件的编码：
UTF-8
文件的读取操作
文件的写入写出操作
'''
'''
open函数打开文件(name,mode,encoding)
name:名称，可以包含路径
mode:打开模式,r:只读,w:删除原有内容,覆盖写入,a:追加写入
encoding:编码,一般使用UTF-8
'''
f = open('D:/source/py_sourse/测试.txt','r',encoding = 'UTF-8')
#read方法
# print(f'读取10个字节的结果:{f.read(10)}')
# print(f'读取所有字节的结果:{f.read()}')
print('------------------------------------')
#readlines方法(读取所有行)   (结果存入列表)
# lines = f.readlines()
# print(f'lines对象的类型是:{type(lines)}')
# print(f'lines对象的结果是:{lines}')
#readline方法(读取一行)
line = f.readline()
print(f'line对象的类型是:{type(line)}')
print(f'line对象的结果是:{line}')


#for循环读取文件行
for line in f:
    print(f'每一行数据是:{line}')

# 关闭文件
f.close()
# with open 语法
with open('D:/source/py_sourse/测试.txt','r',encoding = 'UTF-8') as f:
    for line in f:
        print(f'每一行数据是:{line}')
#   -------------------------------------------------------------  


#文件的写入操作
#write ,flush  
#write操作将数据写入内存，flush刷新缓冲区，将数据真正写入硬盘
f = open('D:/source/py_sourse/test.txt', 'w', encoding='UTF-8')
f.write('hello world!')
f.flush()
f.close()
#文件的追加操作
f = open('D:/source/py_sourse/test.txt', 'a', encoding='UTF-8')
f.write('\nadd 1')
f.write('add 2')
f.flush()
f.close()