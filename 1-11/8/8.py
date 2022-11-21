# Предложите пользователю ввести общую сумму счета, а затем запросите общее количество участников обеда.
# Разделите сумму счета на количество участников и выведите сумму,
# которую должен заплатить каждый участник.

sum = int(input('Enter the amount of lunch: '))
person = int(input('Enter the number of persons: '))
new_sum = sum/person
print('each person must pay', new_sum)
