from datetime import datetime


def validate_record(name, birth_date):
    try:
        datetime.strptime(birth_date, '%d.%m.%Y')
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {birth_date}')
        return False
    else:
        return True


def process_people(data):
    good_count = 0
    bad_count = 0
    good_bad = {}
    for el in data:
        name = el[0]
        birth_date = el[1]
        if validate_record(name, birth_date):
            good_count += 1
        else:
            bad_count += 1
    good_bad['good'] = good_count
    good_bad['bad'] = bad_count
    print(f'Корректных записей: {good_count}')
    print(f'Некорректных записей: {bad_count}')
    return good_bad


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
