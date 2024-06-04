from utils import *

"""
#load the model we created, and print its summary
loaded_model = keras.models.load_model("firstModel.keras")
print(loaded_model.summary())

loss, acc = loaded_model.evaluate(X_test, Y_test, verbose=2)
print('Model accuracy: {:5.2f}%'.format(100 * acc))

d = DrawDetermine()
#while True:
"""
MODELNAME = "Model2.keras"

class DrawModel:
    def __init__(self):
        self.loaded_model = keras.models.load_model(MODELNAME)

    def predict(self, image):
        prediction = self.loaded_model.predict(image)
        prediction_probs = tf.nn.softmax(prediction)
        yhat = np.argmax(prediction_probs)
        return yhat
