import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import json


def download_image(url, folder):
    filename = os.path.join(folder, url.split("/")[-1])  # add path
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Изображение сохранено: {filename}')
    else:
        print(f'Ошибка загрузки изображения: {url}')


url = "https://k-telecom.org/oborudovanie/"
json_name = "data.json"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    popular_items_html = soup.find_all("a", class_="product-card__wrapper")

    img_tags = soup.find_all('img', class_="product-card__img")
    img_urls = [img['data-src'] for img in img_tags if 'data-src' in img.attrs]

    data = []

    for number, item_block in enumerate(popular_items_html):
        name = item_block.find("h6", class_="product-card__title h6").get_text().rstrip("\n")
        description = item_block.find("div", class_="product-card__desc")
        price = item_block.find("div", class_="product-card__price h5").get_text()

        try:  # есть блоки без span и текст с лишними символами :)
            description = description.find("span").get_text().lstrip("\n").rstrip(" ")
        except Exception as _:
            description = description.get_text().lstrip("\n").lstrip().rstrip(" ")

        img_url = img_urls[number]
        if img_url.startswith('http'):
            full_url = img_url
        else:
            full_url = f'{url}/{img_url}'
        download_image(full_url, folder="src")

        element = {
            "name": name,
            "description": description,
            "price": price,
            "img_url": img_url
        }
        data.append(element)

        print(number)
        print(name)
        print(description)
        print(price)
        print(f"image_url={img_url}")
        print()

    with open(json_name, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

else:
    print(f"Ошибка: не удалось получить доступ к {url}, статус код: {response.status_code}")
