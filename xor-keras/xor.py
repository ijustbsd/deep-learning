# https://keras.io/getting-started/sequential-model-guide/
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from keras.callbacks import TensorBoard
import numpy as np

dataset = np.array([
    [0, 0], [0, 1], [1, 0], [1, 1]
])
result = np.array([
    [0], [1], [1], [0]
])

# https://keras.io/models/sequential/
model = Sequential([
    # https://keras.io/layers/core/#dense
    Dense(2, input_dim=2, kernel_initializer='ones'),
    # https://keras.io/activations/
    Activation('tanh'),
    Dense(1),
    Activation('tanh')
])

# https://keras.io/optimizers/#sgd
sgd = SGD(lr=.5)
model.compile(optimizer=sgd, loss='mse')

tensorboard = TensorBoard(log_dir='logs', write_graph=True)

# https://keras.io/getting-started/sequential-model-guide/#training
model.fit(dataset, result, epochs=200, verbose=False, callbacks=[tensorboard])
print(model.predict_proba(dataset))

'''
[[0.00565296]
 [0.94289315]
 [0.94289315]
 [0.00881029]]
'''
