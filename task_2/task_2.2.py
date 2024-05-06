try:
    tickets = int(input('Количество билетов: '))
    user_tic = 0
    for age in range(tickets):
        age = int(input('Возраст посетителя: '))
        if 14 >= age < 18:
            user_tic += 0
            print('Бесплатный вход')
        elif 18 <= age < 25:
            user_tic += 990
            print('Стоимость билета 990 руб.')
        elif 25 <= age < 100:
            user_tic += 1390
            print('Полная стоимость 1390 руб.')
        else:
            print('Не верный ввод возраста: ', age)
    print('Сумма к оплате: ', user_tic)

except ValueError as error:
    print(error)
    print("!!!Не верный формат ввода!!!")
if tickets >= 4:
    user_tic -= (user_tic * 10 / 100)
    print('Сумма к оплате со скидкой: ', round(user_tic))
    print('Итоговая сумма: ', round(user_tic), 'руб.')