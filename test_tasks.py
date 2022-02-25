# Задание 1
# Внутри set используется HashTable, сложность создания O(k), в худшем случае O(k^2)
# Поиск в HashTable имеет сложность O(1), в худшем случае O(k)
# Пробежатся по массиву - O(n)
# Резульитрующая сложность O(n)
# А в худшем случае O(n * k)

def task_1(array_1, array_2):
    to_remove = set(array_2)
    return [it for it in array_1 if it not in to_remove]


# Задание 2
def filter_0(array):
    index = 0
    while index < len(array):
        if array[index] == 0:
            del array[index]
        else:
            index += 1
    return array
