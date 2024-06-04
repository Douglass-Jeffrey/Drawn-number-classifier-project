# Douglass Jeffrey simple machine learning multiclass classification project
from utils import *

tf.keras.datasets.mnist.load_data(path='mnist.npz')
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

#print(x_train[1].shape)
tf.random.set_seed(14)

#maybe something simple to start off
#generate a simple 4 layer model

model = keras.Sequential()
model.add(layers.Flatten(input_shape=x_train[1].shape))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=40)
model.save("Model2.keras")
model.summary()


