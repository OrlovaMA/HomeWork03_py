# Задача 5
# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,n):
    lst1 = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(lst1)
    lst2 = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(lst2)

negofibonacci.reverse()
fibonacci.insert(0, 0)
print(f'Для {n} - {negofibonacci+fibonacci}')