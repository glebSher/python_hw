# Задание №6
# 📌 Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from collections import namedtuple
from pathlib import Path
import logging
import argparse

logging.basicConfig(level=logging.INFO, filename='dir_Info.txt', encoding='utf-8')
logger = logging.getLogger('__name__')
File = namedtuple('File', 'name, extension, dir, parent')

def read_dir(file_path: Path):
    for file in file_path.iterdir():
        # print(file.stem)
        object = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(object)
        if object.dir:
            read_dir(Path(object.parent) / object.name)

def walker():
    parser = argparse.ArgumentParser(prog='read_dir()',
                                     description='Обход каталога с данных сохранением в файл')
    parser.add_argument('-f', '--file_path', help='Какую директорию анализируем', required=True, type=Path)
    args = parser.parse_args()
    return read_dir(args.file_path)

if __name__ == '__main__':
    # read_dir(Path('C:\\Users\\Глеб\\Downloads\\GB.RU\\18_Погружение в Python\\Seminars\\seminar_1\\first_project'))
    walker()