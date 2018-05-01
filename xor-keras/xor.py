from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
import numpy as np

dataset = np.array([
    [0, 0], [0, 1], [1, 0], [1, 1]
])
result = np.array([
    [0], [1], [1], [0]
])

model = Sequential([
    Dense(2, input_dim=2, kernel_initializer='ones'),
    Activation('tanh'),
    Dense(1),
    Activation('tanh')
])

sgd = SGD(lr=.5)
model.compile(optimizer=sgd, loss='mse')

model.fit(dataset, result, epochs=200)
print(model.predict_proba(dataset))

'''
[[0.00565296]
 [0.94289315]
 [0.94289315]
 [0.00881029]]
'''
