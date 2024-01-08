# Задание №5
# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

from datetime import datetime
import logging
import argparse

MONTHS = ('', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл',
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

    count = int(count[0]) if count.isdigit() else int(count[0])
    week_day = int(week_day) if week_day.isdigit() else DAYS.index(week_day[:4])
    month = MONTHS.index(month[:3])
    tmp = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == week_day:
            tmp += 1
            if tmp == count:
                return date


def parser():
    new_parser = argparse.ArgumentParser(prog='get_date()',
                                         description='Получаем дату по дню недели и месяцу',
                                         epilog='При отсутствии параметров, возьмем текущий день недели и месяц'
                                         )
    new_parser.add_argument('-c', '--count', default=1, help='Какой день недели по счету')
    new_parser.add_argument('-w', '--week_day', default=datetime.now().weekday(), help='Какой день недели')
    new_parser.add_argument('-m', '--month', default=datetime.now().month, help='Какой месяц')
    args = new_parser.parse_args()
    print(args.week_day)

    return get_date(f'{args.count} {args.week_day} {args.month}')

if __name__ == '__main__':
    print(get_date('1-й четверг ноября'))
    print(get_date('3-я среда мая'))
    print(parser())
    # print(datetime.now().day_name())
