def transform_list(numbers, transform_function=None):
    """
    Преобразует список numbers с помощью функции transform_function.
    Если transform_function не задана, возвращает копию исходного списка.

    :param numbers: список чисел
    :param transform_function: функция преобразования (необязательный параметр)
    :return: новый список с преобразованными элементами
    """
    if transform_function is None:
        return numbers.copy()
    else:
        return [transform_function(x) for x in numbers]

print(transform_list([1, 2, 3])) 
print(transform_list([1, 2, 3], transform_function=lambda x: x * 2))
