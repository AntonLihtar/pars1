"""Скрипт принимает отдельный URL или список URL адресов,
и скачивает файлы в эту же папку с этим скриптом."""

import os
import zipfile

import requests


def save_file(file_link: str, zip_flag=False):
    """Zip_flag нужен только для зип архивов,
     функция начнет возвращать имя файла."""

    file_name = file_link.split('/')[-1]  # назначаем имя

    # Получаем контент по ссылке и записываем в файл
    download_file = requests.get(file_link, allow_redirects=True)
    with open(file_name, 'wb') as f:
        f.write(download_file.content)

    if zip_flag:
        return file_name
    else:
        print(f'Save: OK >>   {file_name}')


def save_many_files(links_to_files):
    """Принимает сет, список, кортеж ссылок"""
    for link in links_to_files:
        save_file(link)
    print('All files are saved')


def save_zip_unpack(zip_link: str, del_file=True):
    """Ф. скачивает zip и распаковывает,
     архив после распаковки удаляется при del_file=True. """

    file_name = save_file(zip_link, True)

    dir_name = file_name.split('.')[0]
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    with (zipfile.ZipFile(file_name, 'r')) as zf:
        zf.extractall(f'./{dir_name}')  # здесь можно изменить путь к архиву

    if del_file:  # удаляет Zip после распаковки
        os.remove(file_name)
    print(f'Extends: OK >>   {file_name}')


def save_many_zip_unpack(links_to_zip):
    """Принимает сет, список, кортеж ссылок"""
    for x in links_to_zip:
        save_zip_unpack(x)
    print('All zips are unpacked')


if __name__ == '__main__':
    url1 = 'https://amiel.club/uploads/posts/2022-03/1647628341_1-amiel-club-p-klassnie-kartinki-dlya-devochek-1.jpg'
    url = 'https://static.tildacdn.com/downloads/Tilda_Icons_1_Education.zip'
    save_file(url1)
    save_zip_unpack(url)
