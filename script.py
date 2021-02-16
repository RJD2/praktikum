# Задача 1
list1 = [1, 2, 4, 5, 6, 7]
list2 = [2, 5, 7, 3, 1]
result = set(list1) - set(list2)  # Сложность O(n)
print(*result)


# Задача 2
array = [0, 2, 0, 10, 23, 6, 0, 4, 13]

while True:
    try:
        array.remove(0)
    except ValueError:
        break

print(array)
