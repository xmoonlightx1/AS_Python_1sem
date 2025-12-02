K = int(input("Введите K (0 < K < 10): "))
filename = "input.txt" 

with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

if len(lines) <= K:
    print("В файле недостаточно строк.")
else:
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines[:-K])

print(f"Удалены последние {K} строк из файла '{filename}'.")

