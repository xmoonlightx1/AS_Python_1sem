# а) Добавляет новый ключ и значение в словарь
def add_key_value(d, key, value):
    d[key] = value
    return d

# б) Выводит все уникальные значения из словаря
def unique_values(d):
    return set(d.values())

# в) Подсчитывает общее количество элементов в списках, которые являются значениями в словаре
def count_elements_in_lists(d):
    total = 0
    for v in d.values():
        if isinstance(v, list):
            total += len(v)
    return total


# а)
d1 = {1: 2, 3: 4}
d1 = add_key_value(d1, 5, 6)
print("а) Добавленный ключ и значение:", d1)

# б)
d2 = {1: 2, 3: 4, 5: 2}
print("б) Уникальные значения:", unique_values(d2))  

# в)
d3 = {1: [2, 3, 4], 3: [5, 6, 7], 5: [8, 9, 0]}
print("в) Общее количество элементов в списках:", count_elements_in_lists(d3))
