#Задача №2
def sum_excluding_sublist(lst, K, L):
    total_sum = sum(lst)
    excluded_sum = sum(lst[K-1:L])
    return total_sum - excluded_sum

lst = [10, 20, 30, 40, 50, 60]
K = 2
L = 4

result = sum_excluding_sublist(lst, K, L)
print(f"Сумма всех элементов кроме с {K} по {L}: {result}")
