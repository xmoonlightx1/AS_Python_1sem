import math


s = 5 + 6 * 12
print("s=", s)

a = 5
b = 6
c = 12
d = b * c
s = a + d
print("s=", s)

a = 5
b = 6
S = a * b
print("Площадь:", S)

x = 7
y = 12
z = x + y
print("Сумма:", z)

def area(a, b):
    return a * b

print("Площадь:", area(8, 7))

def f(x):
    return (3 + x) * 2

print(f(5))

def g(x):
    return 3 + x * 2

print(g(5))  # 13

def sqrt_fn(x):
    return math.sqrt(x)

print(sqrt_fn(25))

def average(a, b, c):
    return (a + b + c) / 3

print(average(5, 7, 9))

def fact_fn(n):
    return math.factorial(n)

print(fact_fn(5))

def stats(a, b, c):
    total = a + b + c
    average = total / 3
    maximum = max(a, b, c)
    print("Сумма:", total)
    print("Среднее:", average)
    print("Максимум:", maximum)
    return total, average, maximum

print(stats(5, 7, 9))

a = 7
a = a + 3
print("a=", a)
a += 1  # эквивалентно a = a + 1
print("a=", a)
a -= 2  # эквивалентно a = a - 2
print("a=", a)
a *= 4  # эквивалентно a = a * 4
print("a=", a)
a /= 2  # эквивалентно a = a / 2
print("a=", a)
a %= 3  # эквивалентно a = a % 3
print("a=", a)
a **= 2 # эквивалентно a = a ** 2
print("a=", a)
a //= 4 # эквивалентно a = a // 4
print("a=", a)

attempts = 0
print("attempts=", attempts)
attempts += 1  # новая попытка
print("attempts=", attempts)
attempts += 1  # еще одна попытка
print("attempts=", attempts)

name = "Python"
greeting = 'Привет, мир!'
message = """Это многострочная
строка"""

first = "Hello"
second = "student"
result = first + " " + second

text = "Python"
text = text + " 3.10"

a = 5
b = 3
print(a, b, "сумма:", a + b)
print(f"{a} {b} сумма: {a + b}")

city = "Москва"
temp = 20
print(f"Сегодня в {city} температура {temp}°C")

s = "Баллы: %d, оценка: %s" % (28, "отлично")
print(s)

student = "Антон"
score = 95
print("Имя: {}, баллы: {}".format(student, score))
print("Оценка: {b}, студент: {a}".format(a="Дина", b=87))

print("Первый ряд\nВторой ряд\tТретий столбец")

print(1, 2, 3, sep='---')
print("Старт", end='...')
print("Финиш")

pi = 3.14159265
print(f"Pi: {pi:.2f}")

name = "Лиза"
print(f"|{name:^10}|")  # |   Лиза   |
print(f"|{name:<10}|")  # |Лиза      |
print(f"|{name:>10}|")  # |      Лиза|

s = 10
print(f"{name=} {s=}")

def student_info(name, age=18, score=100):
    print(f"Студент: {name}")
    print(f"Возраст: {age}")
    print(f"Баллы: {score}")
    if score >= 85:
        return "Отличник"
    elif score >= 60:
        return "Хорошист"
    else:
        return "Нужно подтянуть"

print(student_info(name="Саша"))
print(student_info(name="Сережа", age=19))
print(student_info(name="Славик", age=22, score=70))
print(student_info("Вова", age=20, score=80))
print(student_info("Гриша", 21, score=90))
