from selenium import webdriver as wd     #用于操作浏览器
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options           #用于设置google浏览器的无头模式
from time import sleep

q1 = Options()
#禁用沙盒模式
q1.add_argument('--no-sandbox')
#保持浏览器的打开状态
q1.add_experimental_option(name='detach', value=True)

#创建并启动浏览器
a1 = wd.Chrome(service = Service('chromedriver.exe'), options=q1)

#打开一个网页
a1.get('https://www.baidu.com')
a1.set_window_position(400, 100)  #设置窗口位置
a1.set_window_size(800, 600)      #设置窗口大小
a1.maximize_window()  #最大化窗口
a1.get_screenshot_as_file('baidu.png')  #截图并保存
#等待2秒
sleep(2)
a1.minimize_window()  #最小化窗口
sleep(2)
#关闭当前标签页
a1.close()