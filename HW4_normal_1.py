# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
        lst = [1, 1]

        i = 2
        while i <= m:
            lst.append(lst[i - 1] + lst[i - 2])
            i += 1

        return lst[n:]

print(fibonacci())








