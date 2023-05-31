number = input('Введите число: ')
try:
    number = int(number)**2
    print(number)
except ValueError:
    print('Вы ввели не число! попробуйте еще раз')
