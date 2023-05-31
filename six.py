try:
    a, b = int(input('Введите а: ')), int(input('Введите b: '))
    x = -b/a
    print(x)
except ValueError:
    print('Вы ввели не число, попробуйте еще раз :/')