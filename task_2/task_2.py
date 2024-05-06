tickets = int(input('Количество билетов: '))
user_tic = 0
for age in range(tickets):
    age = int(input('Возраст посетителя: '))
    if age < 18:
        user_tic += 0
        print('Бесплатный вход')
    elif 18 <= age < 25:
        user_tic += 990
        print('Стоимость билета 990 руб.')
    elif age >= 25:
        user_tic += 1390
        print('Полная стоимость 1390 руб.')

print('Сумма к оплате: ', user_tic,'руб.')
if tickets >= 4:
    user_tic -= (user_tic * 10 / 100)
    print('Сумма к оплате со скидкой: ', round(user_tic), 'руб.')
    print('Итоговая сумма: ', round(user_tic), 'руб.')