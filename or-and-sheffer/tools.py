import json
from math import fabs

# Логические функции
dis = lambda x, y:  (x + 1 or y + 1) - 1 # Дизъюнкция

con = lambda x, y:  (x + 1 and y + 1) - 1 # Конъюнкция

sheffer = lambda x, y: -(x + 1 and y + 1) + 1 # Штрих Шеффера

f = dis # Какую функцию хотим использовать

# Функиця активации
signum = lambda x: (x > 0) - (x < 0)

# Дельта, на которую нужно изменить вес
# weight_delta = lambda d, x, w: 0.01 * d * x + fabs(w)
weight_delta = lambda d, x, w: 0.01 * d * x

# Веса
weights = json.load(open('weights.json'))

# Сохранение значений весов в файл
save_weights = lambda w: json.dump(w, open('weights.json', 'w'))
