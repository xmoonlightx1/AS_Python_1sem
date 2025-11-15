# Задание №2 с примером
import math

def sum_cos_series(n, x):
    cos_x = math.cos(x)
    total = 0.0
    for k in range(1, n + 1):
        total += (cos_x ** k) / k
    return total

n = 5
x = 1.0
result = sum_cos_series(n, x)
print(f"Сумма ряда для n={n}, x={x}: {result}")
