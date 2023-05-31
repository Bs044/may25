try:
    user_hour = int(input('Введите который у вас час: '))
    user_minute = int(input('Введите которая у вас минута: '))
    hour = 24
    minute = 60
    result1, result2 = hour - user_hour -1, minute - user_minute
    print(f'до следующего дня {result1}:{result2} минуты')
except ValueError:
    print('Вы ввели не число, попробуйте еще раз :/')