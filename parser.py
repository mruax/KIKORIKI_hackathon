import requests
from bs4 import BeautifulSoup

url = "https://k-telecom.org/oborudovanie/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    popular_items_html = soup.find_all("a", class_="product-card__wrapper")

    for number, item_block in enumerate(popular_items_html):
        name = item_block.find("h6", class_="product-card__title h6").get_text().rstrip("\n")
        description = item_block.find("div", class_="product-card__desc")
        price = item_block.find("div", class_="product-card__price h5").get_text()

        try:  # есть блоки без span и текст с лишними символами :)
            description = description.find("span").get_text().lstrip("\n")
        except Exception as _:
            description = description.get_text().lstrip("\n").lstrip()

        print(number)
        print(name)
        print(description)
        print(price)

        print()

else:
    print(f"Ошибка: не удалось получить доступ к {url}, статус код: {response.status_code}")
