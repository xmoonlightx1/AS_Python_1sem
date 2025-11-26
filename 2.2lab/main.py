import math

def Circle(R):
    """
    Вычисляет площадь и длину окружности круга радиуса R.

    Параметры:
    R (float): радиус круга

    Возвращает:
    tuple: (площадь, длина окружности)
    """
    area = math.pi * R ** 2
    circumference = 2 * math.pi * R
    return area, circumference


radius = 5
area, length = Circle(radius)
print(f"Радиус: {radius}")
print(f"Площадь круга: {area:.2f}")
print(f"Длина окружности: {length:.2f}")
