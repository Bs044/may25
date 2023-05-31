user_data = input('Введите сколько км нужно перевести в мили: ')

try:
    user_data = int(user_data)
    result = user_data * 0.621371
    print(f'{result} будет столько миль)')
except ValueError:
    print('Вы ввели не число, попробуйте еще раз :/')
