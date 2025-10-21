N = int(input("Введите целое число N > 1: "))
A = float(input("Введите число A: "))
B = float(input("Введите число B (B >= A): "))

if N <= 1:
    print("N должно быть больше 1")
elif B < A:
    print("B должно быть больше или равно A")
else:
    
    H = (B - A) / N

    points = [A + i * H for i in range(N + 1)]

    print(f"Длина каждого отрезка H = {H}")
    print("Точки разбиения отрезка [A, B]:")
    for p in points:
        print(p)
