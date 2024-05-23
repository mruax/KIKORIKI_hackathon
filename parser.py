import requests
from bs4 import BeautifulSoup

# URL страницы, которую будем парсить
url = 'https://k-telecom.org/oborudovanie/'

# Делаем HTTP GET запрос к указанному URL
response = requests.get(url)

# Проверяем, успешен ли запрос (статус код 200)
if response.status_code == 200:
    # Парсим HTML содержимое страницы с помощью BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Находим все элементы h2 (или другие нужные элементы)
    headlines = soup.find_all('h2')

    # Выводим текст каждого заголовка
    for headline in headlines:
        print(headline.get_text())
else:
    print(f'Ошибка: не удалось получить доступ к {url}, статус код: {response.status_code}')
