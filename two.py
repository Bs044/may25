number1, number2 = input('Введите 1 число: '), input('Введите 2 число: ')
try:
    number1, number2 = int(number1), int(number2)
    result = (number1+number2)/2
    print(result)
except ValueError:
    print('Вы ввели не число, попробуйте еще раз :/')
