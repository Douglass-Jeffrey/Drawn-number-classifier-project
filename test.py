from utils import *

tf.keras.datasets.mnist.load_data(path='mnist.npz')
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

MODELNAME = "Model2.keras"
loaded_model = keras.models.load_model(MODELNAME)
loaded_model.summary()

failures = 0

for i in range(10000):
    test = x_test[i].reshape(1, 28, 28)
    prediction = np.argmax(loaded_model.predict(test))
    #print(prediction)
    if prediction != y_test[i]:
        failures += 1
        print("Prediction failed for", i)

print("Total failures:", failures)





