#Открытие файла с обработкой исключений FileNotFoundError и IOError
filename = input("Введите имя файла: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("Файл не найден")
except IOError:
    print("Ошибка чтения файла")
else:
    print("Файл успешно прочитан")


#Проверка, является ли строка палиндромом, с выбросом исключения, если нет
class NotPalindromeError(Exception):
    pass

def check_palindrome(s):
    s_clean = ''.join(c.lower() for c in s if c.isalnum())  # игнорируем пробелы и знаки препинания
    if s_clean != s_clean[::-1]:
        raise NotPalindromeError("Строка не является палиндромом")
    else:
        print("Строка является палиндромом")

user_input = input("Введите строку: ")

try:
    check_palindrome(user_input)
except NotPalindromeError as e:
    print(e)


#Открытие файла с использованием assert для проверки существования
class NotPalindromeError(Exception):
    pass

def check_palindrome(s):
    s_clean = ''.join(c.lower() for c in s if c.isalnum())  # игнорируем пробелы и знаки препинания
    if s_clean != s_clean[::-1]:
        raise NotPalindromeError("Строка не является палиндромом")
    else:
        print("Строка является палиндромом")

user_input = input("Введите строку: ")

try:
    check_palindrome(user_input)
except NotPalindromeError as e:
    print(e)
