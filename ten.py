try:
    sum_sale = input('Введите общую сумму продаж за месяц: ')
    sum_sale = int(sum_sale)
    result = (sum_sale / 10) + 250
    print(f'Ваша зарплата с процентом от продаж составляет {result}$')
except ValueError:
    print('Вы ввели не число, попробуйте еще раз :/')