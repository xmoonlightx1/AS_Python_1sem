def PowerN(x, n):
    """
    Рекурсивно вычисляет x в степени n.

    :param x: вещественное число, x >= 0
    :param n: целое число (показатель степени)
    :return: x^n
    """
    if n == 0:
        return 1
    elif n > 0:
        return x * PowerN(x, n - 1)
    else: 
        return 1 / PowerN(x, -n)

print(PowerN(2, 3))   
print(PowerN(5, 0))   
print(PowerN(2, -2))  
