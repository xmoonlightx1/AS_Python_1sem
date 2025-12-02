import math
from typing import Tuple, List

Point = Tuple[float, float]

def distance(p1: Point, p2: Point) -> float:
    """Вычисляет расстояние между двумя точками на плоскости."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def distances_between_points(p1: Point, p2: Point, p3: Point) -> List[float]:
    """Возвращает список расстояний между тремя точками: [p1-p2, p2-p3, p3-p1]."""
    d12 = distance(p1, p2)
    d23 = distance(p2, p3)
    d31 = distance(p3, p1)
    return [d12, d23, d31]

def can_form_triangle(sides: List[float]) -> bool:
    """Проверяет, можно ли построить треугольник по заданным сторонам."""
    a, b, c = sorted(sides)
    return a + b > c  # Неравенство треугольника

def perimeter(p1: Point, p2: Point, p3: Point) -> float:
    """Вычисляет периметр треугольника, если он существует. Иначе возвращает 0."""
    sides = distances_between_points(p1, p2, p3)
    if can_form_triangle(sides):
        return sum(sides)
    else:
        return 0.0

def area(p1: Point, p2: Point, p3: Point) -> float:
    """Вычисляет площадь треугольника по формуле Герона, если он существует. Иначе возвращает 0."""
    sides = distances_between_points(p1, p2, p3)
    if not can_form_triangle(sides):
        return 0.0
    s = sum(sides) / 2  # полупериметр
    a, b, c = sides
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


import triangle_utils as tu

p1 = (0, 0)
p2 = (3, 0)
p3 = (0, 4)

distances = tu.distances_between_points(p1, p2, p3)
print(f"Расстояния между точками: {distances}")

perim = tu.perimeter(p1, p2, p3)
if perim > 0:
    print(f"Периметр треугольника: {perim}")
else:
    print("Треугольник по заданным точкам построить нельзя")

area = tu.area(p1, p2, p3)
if area > 0:
    print(f"Площадь треугольника: {area}")
else:
    print("Треугольник по заданным точкам построить нельзя")


