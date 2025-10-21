#Мастер обслуживает 6 станков. Вероятность поломки одного станка в течение дня равна  Во сколько раз вероятность события «в течение дня ровно два станка потребуют ремонта» больше, чем вероятность события «в течение дня ровно 3 станка потребуют ремонта»?
    from math import comb

def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def ratio_of_probabilities(n, p, k1, k2):
    prob_k1 = binomial_probability(n, k1, p)
    prob_k2 = binomial_probability(n, k2, p)
    if prob_k2 == 0:
        return float('inf'), prob_k1, prob_k2
    
    ratio = prob_k1 / prob_k2
    return ratio, prob_k1, prob_k2

# Дано:
n = 6  # количество станков
p = 0.1  # вероятность поломки одного станка в течение дня (пример)

k1 = 2  # событие: ровно 2 станка сломаются
k2 = 3  # событие: ровно 3 станка сломаются

ratio, prob_2, prob_3 = ratio_of_probabilities(n, p, k1, k2)

print(f"Вероятность ровно {k1} станков сломается: {prob_2:.6f}")
print(f"Вероятность ровно {k2} станков сломается: {prob_3:.6f}")
print(f"Во сколько раз вероятность для {k1} больше вероятности для {k2}: {ratio:.4f}")
