from time import sleep
import requests as req
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}
for start_num in range(0,250,25):
    sleep(1)
    try:
        response = req.get(f'https://movie.douban.com//top250?start={start_num}&filter=', headers=headers)
        if response.status_code == 200:
            pass
            #print("Request successful")
            #print(response.text)
        else:
            print(f"Request failed with status code: {response.status_code}")
    except req.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    soup = BeautifulSoup(response.text, 'html.parser')
    all_film_name = soup.find_all('span', attrs={'class': 'title'})
    for film in all_film_name:
        title = film.string
        if title.find('/') == -1:
            print(title)
