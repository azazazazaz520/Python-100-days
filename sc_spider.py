import random
from time import sleep
import requests as req
from bs4 import BeautifulSoup
import cloudscraper
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}





if __name__ == '__main__':
    try:
        sleep(random.uniform(1, 3))
        scraper = cloudscraper.create_scraper()  # 创建一个scraper实例
        response = scraper.get('https://uexcorp.space/',headers=headers)  # 发送请求
        if response.status_code == 200:
            print("Request successful")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except req.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

    soup = BeautifulSoup(response.text, 'html.parser')
    goods_name = soup.find_all('span', attrs = {'class': 'text-bold translucent'})
    for goods in goods_name:
        name = goods.string
        print(name)

