# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime
import logging

MONTHS = ('', 'янв', 'февр', 'мар', 'апр', 'мая', 'июн', 'июл',
          'авг', 'сен', 'окт', 'ноя', 'дек')
DAYS = ('поне', 'втор', 'сред', 'четв', 'пятн', 'субб', 'воск')

logging.basicConfig(level=logging.ERROR, filename='loggingError.log', encoding='utf-8')
logger = logging.getLogger('__name__')


def get_date(date: str):
    try:
        count, week_day, month = date.split()
    except ValueError as e:
        logger.error(f'Не удалось разбить строку на компоненты')
        return

    count = int(count[0])
    week_day = DAYS.index(week_day[:4])
    month = MONTHS.index(month[:3])
    tmp = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=datetime.now().year)
        # print(date)
        if date.weekday() == week_day:
            tmp += 1
            if tmp == count:
                return date


if __name__ == '__main__':
    print(get_date('1-й четверг ноября'))
    print(get_date('3-я среда мая'))
