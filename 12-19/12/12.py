# Предложите пользователю ввести два числа. Если первое число больше второго,
# сначала выведите второе число, а потом первое.
# В противном случае выведите сначала первое число, а потом второе.

num_1 = int(input('enter first number: '))
num_2 = int(input('enter second number: '))
if num_1 > num_2:
    print(num_2, num_1)

else:
    print(num_1, num_2)
