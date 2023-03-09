"""Парсер страницы сайта tilda.cc, вытаскивает с данной страницы ссылки архивов иконок
Для скачивания и распаковки использую свой скрипт downloader_z.py
Этот скрипт был создан был для скачивания иконок и обзора парсинка на Python
"""

import requests
from bs4 import BeautifulSoup

URL = "https://tilda.cc/ru/free-icons/"


def set_add_result_set(result_set, set_link: set[str]):
    """Вытаскиваем ссылки из тегов и добавляем в сет"""
    for rs in result_set:
        set_link.add(rs.find("a").get("href"))


def get_urls() -> set[str]:
    res_req = requests.get(URL)

    # Преобразуем код в дерево объектов lxml # считается самым быстрым парсером
    soup = BeautifulSoup(res_req.text, "lxml")

    many_links = set()  # сюда будем сохранять все ссылки

    # выбираем ссылки со страницы
    user_name = soup.find_all("div", class_="t390__title")
    set_add_result_set(user_name, many_links)
    # 1й запрос достает не все ссылки(добиваем)
    user_name2 = soup.find_all("div", class_="t432__wraptwo")
    set_add_result_set(user_name2, many_links)
    return many_links


if __name__ == '__main__':
    res = get_urls()
    print(len(res))
