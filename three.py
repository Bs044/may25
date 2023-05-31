dlina = input('Введите длину стороны квадрата: ')

try:
    dlina = int(dlina)
    result = dlina * dlina
    print(f'{result} площадь квадрата')
except ValueError:
    print('Вы ввели не число, попробуйте еще раз :/')
