# Предложите пользователю ввести число, меньшее 20.
# Если введенное число больше или равно 20, выведите сообщение «Too high»;
# в противном случае выведите сообщение «Thank you».

num = int(input('Введите число меньшее 20: '))
if num >= 20:
    print('Слишком больше число')

else:
    print('Спасибо')
