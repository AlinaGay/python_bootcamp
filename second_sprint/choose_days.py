from datetime import datetime
from random import sample


def choose_days():
    first_month_half = list(range(1, 16))

    random_days = sample(first_month_half, k=3)
    sorted_days = sorted(random_days)

    now = datetime.now()

    for i in range(len(sorted_days)):
        practice_day = datetime.replace(now, day=sorted_days[i])
        practice_day = datetime.strftime(practice_day, "%d.%M.%Y")
        print(f'{i+1}-е занятие: {practice_day}')


choose_days()
