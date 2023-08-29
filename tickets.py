tickets = int(input('Введите количество билетов\n'))
all_price = 0
for i in range(tickets):
    age = int(input(f'Укажите возраст {i + 1} посетителя\n'))
    if age < 18:
        all_price += 0
    elif 18 <= age < 25:
        all_price += 990
    elif 25 <= age:
        all_price += 1390
if tickets > 3:
    print('Сумма к оплате с учетом скидки', int(all_price - (all_price / 100 * 10)))
else:
    print('Сумма к оплате', all_price)