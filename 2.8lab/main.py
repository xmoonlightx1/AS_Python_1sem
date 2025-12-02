with open("f.txt", "r", encoding="utf-8") as file_f:
    numbers = list(map(int, file_f.read().split()))

positives = [num for num in numbers if num > 0]
negatives = [num for num in numbers if num < 0]

if len(positives) != len(negatives):
    print("Количество положительных и отрицательных чисел не совпадает!")
else:
    with open("g.txt", "w", encoding="utf-8") as file_g:
        for num in positives + negatives:
            file_g.write(str(num) + " ")
