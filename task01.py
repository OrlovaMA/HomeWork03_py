# Задача 1
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётных индексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]
print(lst)
sum = 0
for i in range(len(lst)):
    if i %  2 != 0:
        sum += lst[i]
print(f'Сумма элементов списка, стоящих на нечётных индексах:', sum)
