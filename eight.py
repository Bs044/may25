try:
    number = int(input('Введите трехзначное число: '))
    result = (number/10) % 10
    result = int(result)
    print(result)
except ValueError:
    print('Вы ввели не число, попробуйте еще раз :/')