# Предложите пользователю ввести его имя и возраст. Увеличьте возраст на 1 и вы- ведите сообщение:
# [имя] next birthday you will be [новый возраст].

name = input('please ente your first name: ')
age = int(input('please ente your age: '))
age = age+1
print(name, 'next birthday you will be', age)
