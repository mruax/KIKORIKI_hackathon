import json
import os

import requests
from bs4 import BeautifulSoup

from settings import main_url, json_name


# from pathlib import Path


def download_image(url, folder):
    filename = os.path.join(folder, url.split("/")[-1])  # add path
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Изображение сохранено: {filename}')
    else:
        print(f'Ошибка загрузки изображения: {url}')


def get_items(url=main_url, page_type=0):
    """
    Возвращает информацию о продуктах с разных url.

    :param url: Адрес страницы
    :param page_type: int, 0 - популярные предложения, 1 - роутеры, 2 - телевидение, 3 - видеонаблюдение
    :return: None
    """
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        popular_items_html = soup.find_all("a", class_="product-card__wrapper")
        match page_type:
            case 0:
                header = soup.find('h2', class_="products-slider-block__title block__title").get_text()
            case 1:
                header = soup.find('h1', class_="products-list-cat-block__title block__title").get_text()
                popular_items_html = soup.find('ul', class_="products__list").find_all("a", class_="product-card__wrapper")
            case 2:
                header = soup.find('h1', class_="recommend-products-block__title block__title").get_text()
            case 3:
                header = soup.find('h1', class_="page__title").get_text()
            case _:
                header = "Товары"

        img_tags = soup.find_all('img', class_="product-card__img")
        img_urls = [img['data-src'] for img in img_tags if 'data-src' in img.attrs]

        data = []
        header = header.rstrip().lstrip()
        print(f"{header}:")

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
                full_url = f'{main_url}/{img_url}'
            download_image(full_url, folder="src")

            element = {
                "name": name,
                "description": description,
                "price": price,
                "img_url": img_url
            }
            data.append(element)

            print(f"Продукт №{number + 1}")
            print(name)
            print(description)
            print(price)
            print(f"image_url={img_url}")
            print()

        with open(json_name, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        print(f"Ошибка: не удалось получить доступ к {main_url}, статус код: {response.status_code}")


def get_all_products():
    response = requests.get(main_url)
    all_products = None
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        all_products_tags = soup.find_all('a', class_="shop-cats-block__item shop-cats-block__item_cat")
        all_products = [product_block['href'] for product_block in all_products_tags if 'href' in product_block.attrs]
    else:
        print(f"Ошибка: не удалось получить доступ к {main_url}, статус код: {response.status_code}")
    return all_products


def get_routers(url):
    get_items(url, page_type=1)


def get_televisors(url):
    get_items(url, page_type=2)


def get_cctv(url):
    get_items(url, page_type=3)


# if __name__ == "__main__":
#     get_items()
#     all_products = get_all_products()
#     print(all_products)
#     get_items(url=all_products[0], page_type=1)
#     get_items(url=all_products[0] + "/page/2", page_type=1)  # костыльно, но парсим вторую страницу
#     get_items(url=all_products[1], page_type=2)
#     get_items(url=all_products[2], page_type=3)

