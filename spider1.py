import requests as req
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

try:
    response = req.get('https://movie.douban.com/', headers=headers)
    if response.status_code == 200:
        print("Request successful")
        #print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
except req.exceptions.RequestException as e:
    print(f"Error occurred: {e}")


soup = BeautifulSoup(response.text, 'html.parser')
all_film_name = soup.find_all('li', class_='title')
for film in all_film_name:
    print(film.get_text(strip=True))