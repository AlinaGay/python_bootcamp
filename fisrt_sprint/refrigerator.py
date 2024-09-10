from decimal import Decimal
from datetime import datetime


goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime(2023, 7, 15).date()},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime(2023, 8, 1).date()},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}


def add(items, title, amount, expiration_date=None):
    if expiration_date is not None:
        # expiration_date= datetime.strptime(expiration_date, '%Y-%m-%d')
        
        expiration_date= datetime.strptime(expiration_date, '%Y-%m-%d').date()
    if items.get(title) == None:
        items[title] = [{'amount': amount, 'expiration_date': expiration_date}]     
    else:
        items[title].append({'amount': amount, 'expiration_date': expiration_date})


def add_by_note(items, note):
    note_list = list(note.split(" "))
    if '-' in note_list[-1]:
        expiration_date = note_list[-1]
        amount = Decimal(note_list[-2])
        title = ' '.join(note_list[:-2])
        add(items, title, amount, expiration_date)
    else:
        amount = Decimal(note_list[-1])
        title = ' '.join(note_list[:-1])
        add(items, title, amount)


def find(items, needle):
    needle_list = []
    for title in items.keys():
        if needle.lower() in title.lower():
            needle_list.append(title)
    return needle_list


def amount(items, needle):
    total_amount = Decimal('0')
    for title, value in items.items():
        if needle.lower() in title.lower():
            count = len(value)
            for i in range(count):
                total_amount += value[i]['amount']
    return total_amount


def expire(items, in_advance_days=0):
    today = datetime.today().date()
    expired_product_list = []

    if in_advance_days == None:
        in_advance_days = 0
    for title, value in items.items():
        count = len(value)
        for i in range(count):
            if value[i]['expiration_date'] != None:
                difference = (value[i]['expiration_date'] - today).days
                if difference <= in_advance_days:
                    if expired_product_list != []:
                        if expired_product_list[-1][0] == title:
                            expired_product_list[-1][-1] += value[i]['amount']
                            print(expired_product_list[-1][0])
                        else:
                            expired_product = [title, value[i]['amount']]
                            expired_product_list.append(expired_product)    
        
                    else:
                        expired_product = [title, value[i]['amount']]
                        expired_product_list.append(expired_product)
    expired_product_tuple_list = [tuple(expired_product) for expired_product in expired_product_list]                   
    return expired_product_tuple_list


add(goods, 'Молоко', Decimal('1.6'), '2024-10-28')
print(goods) 
add_by_note(goods, 'Вода газированная 4 2023-07-15')
print(goods)
print(find(goods, 'Вода')) 
print(amount(goods, 'Яйца'))
print(expire(goods, 2))
