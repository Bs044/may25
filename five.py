number1, number2 = input('Введите 1 число: '), input('Введите 2 число: ')
try:
    number1, number2 = int(number1), int(number2)
    result1, result2, result3, result4 = number1 + number2,  number1 - number2,  number1 / number2,  number1 * number2
    print(f'{number1} + {number2} = {result1}, {number1} - {number2} = {result2}, {number1} / {number2} = {result3}, {number1} * {number2} = {result4}')
except ValueError:
    print('Вы ввели не число, попробуйте еще раз :/')
