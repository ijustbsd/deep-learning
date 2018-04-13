import tools

x1 = int(input('Enter x1: '))
x2 = int(input('Enter x2: '))

correct = tools.f(x1, x2)
neuron_output = tools.weights[0] + tools.weights[1] * x1 + tools.weights[2] * x2
result = tools.signum(neuron_output)

print('Result:', result)
print('Correct answer:', correct)
