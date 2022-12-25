# Задача 2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiplication(lst):
    multiplication = []
    for i in range((len(lst)+1)//2):
        multiplication.append(lst[i]*lst[len(lst)-1-i])
    return multiplication

lst = [2,3,4,5,6]
print(lst)
print(multiplication(lst))