import tools

dataset = [
    [-1, -1],
    [1, -1],
    [-1, 1],
    [1, 1]
]

weights = tools.weights

def one_epoch():
    is_changed = 0
    for x in dataset:
        x1, x2 = x
        correct = tools.f(x1, x2)
        neuron_output = weights[0] + weights[1] * x1 + weights[2] * x2
        result = tools.signum(neuron_output)

        d = correct - result

        if not d:
            continue

        weights[0] += tools.weight_delta(d, 1, weights[1])
        weights[1] += tools.weight_delta(d, x1, weights[1])
        weights[2] += tools.weight_delta(d, x2, weights[2])
        tools.save_weights(weights)

        is_changed = 1

    return is_changed

i = 0
while one_epoch():
    i += 1
print(i, 'epochs passed.')

# Тесты
for x in dataset:
    x1, x2 = x
    correct = tools.f(x1, x2)
    neuron_output = weights[0] + weights[1] * x1 + weights[2] * x2
    result = tools.signum(neuron_output)
    if result != correct:
        print('Error! Input values: ({}, {})'.format(*x))
        break
