# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


from typing import Callable
import logging

FORMAT = '{levelname} - {asctime}.{msg}'
logging.basicConfig(level=logging.INFO, filename='loggingInfo.log',
                    encoding='utf-8', format=FORMAT, style='{')
logger = logging.getLogger('__name__')


def my_logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        dict_json = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dict_json['result'] = result
        logger.info(f'Функция: {func.__name__}(). Аргументы: {dict_json.keys()}. Результат: {result}')

        return result

    return wrapper


@my_logger
def get_all(*args: list, **kwargs) -> int:
    return sum(args)


if __name__ == '__main__':
    get_all(42, 6, x='hello', y=12345, z=True)
