# Я считаю, что алгоритм Quick Sort является самым оптимальным, т.к работает
# по принципу разделяй и властвуй.
# Преимущества: скорость и простота реализации.
# Недостатки: рекурсивность.
# Лучшее время выполнения o(n)
# Среднее время выполнения O(n log n)
# Худшее время выполнения O(n^2)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
