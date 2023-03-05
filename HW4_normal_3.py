# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(filter_func, items):
    result = []
    for item in items:
        if filter_func(item):
            result.append(item)

    return result

my_result = my_filter(lambda x: x>5, [1, 5, 10, 16, 7, 8])
print(my_result)