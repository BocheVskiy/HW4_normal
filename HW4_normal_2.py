# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


#def sort_to_max():



#   print("Введите список для сортировки: ")
#   num = list(map(int, input().split())))
#   n = len(num)
#   for i in range(0, n-1):
#       for j in range(0, n-1-i):
#               if num[i] > num[i + 1]:
#               num[i], num[i+1] = num[i+1], num[i]
#
#  print(*num)

num = [2, 4, 5, 8, 1, 3, 9]
n = len(num)
for i in range(0, n-1):
    for j in range(0, n-1-i):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

print(*num)