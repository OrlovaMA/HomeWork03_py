# Задача 4
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 10.01] => 0.19

def difference (list):
    maxmin = []
    for i in range(len(list)):
        if list[i]%1 != 0:
            maxmin.append(list[i]%1)
    return max(maxmin) - min(maxmin)

lst1 = [1.10, 1.20, 3.10, 5, 10.01]
print(lst1)
result = difference(lst1)
print(f'Разница между максимальным и минимальным значением дробной части =', round(result,2))
