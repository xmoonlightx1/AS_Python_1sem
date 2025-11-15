#Задача №2
def first_and_last_two_chars(s):
    if len(s) < 2:
        return "Длина строки меньше двух"
    else:
        return s[:2] + s[-2:]

s = input("Введите строку: ")
result = first_and_last_two_chars(s)
print(result)
