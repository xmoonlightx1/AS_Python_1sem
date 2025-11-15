#Задача №2
def positive_sorted(lst):
    positives = [x for x in lst if x > 0]
    positives.sort()
    return positives

lst = [3, -1, 0, 7, -5, 2, 10]
result = positive_sorted(lst)
print(result)
