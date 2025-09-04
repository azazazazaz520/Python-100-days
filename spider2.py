import requests as req
from time import sleep
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'cookie': '_xsrf=GhHQ6Y5V3vF3N4JlBTO0bHLN1NFebrBl; _zap=802128b4-268a-4f59-9daa-8c356f03f808; d_c0=ZpCTLBuKsxqPTlcsDzdRCoTP8GY90_ZWEYk=|1751505289; q_c1=eed333755d754acfa4f2b883066310d9|1752369087000|1752369087000; __zse_ck=004_pYFfB4TJK2=5/u42GRP0GkFWIR5LIVNhDy0iavDxT9GuC4sNZ8KhHn2FMZDUv9y1/J3sdwKhtjntqz26NmTyuMC0ibFsziPpRA1KEcuyC/C9=Ohe0EXtl6ZF1TOTMz89-wHtLO/dy3HudvBukR4zicHJTyfc0cS1o3XY9s7/3zkmx3WClxpCkjHBlyIw4+mjIvi97q0HyA0ObojwNgC3qm422Pi3HxauY8hMpSqRzR/RjA9Wpy7CLEVImhAuO01xZ; z_c0=2|1:0|10:1756548055|4:z_c0|80:MS4xSHVHLUdBQUFBQUFtQUFBQVlBSlZUYWNPb0drY1dTbHVnSEV3R3RzcjhJR3hRTm1SY1ppN3FBPT0=|c62812e6b44cd483efd6039d509a771e57b12c49ebc6ce77002aaf549e734cd4; BEC=ec64a27f4feb1b29e8161db426d61998; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1756548054,1756565497,1756718449,1756993914; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1756993914; HMACCOUNT=4666178BE8F0C529; SESSIONID=f7izHgyAU2rwng9xSJWkxZmUoQYYDJ5dCffgb1HfMWv; JOID=UF4XAk5BjXb2TlsoU8UYJSh3MetJI74ciAE4VRETuwCCJDsVLzsTyJ1NWy9ULRqevr35ZJYBJq2p6K9a9Ste-AI=; osd=VlsVB05HiHTzTl0tUcAYIy11NOtPJrwZiAc9VxQTvQWAITsTKjkWyJtIWSpUKx-cu73_YZQEJqus6qpa8y5c_QI='
}
sleep(0.5)
response = req.get('https://www.zhihu.com/', headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    all_title_name = soup.find_all('a', attrs={'target': "_blank", 'data-za-detail-view-element_name': "Title"})
    for title in all_title_name:
        print(title.string)