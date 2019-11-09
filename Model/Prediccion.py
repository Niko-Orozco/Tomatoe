import numpy as np
from keras_preprocessing.image import load_img, img_to_array
from keras.models import load_model

longitud, altura = 100,100
modelo = './model/models.cnt'
pesos = './model/pesos.cnt'
cnn= load_model(modelo)
cnn.load_weights(pesos)

def Predict(file):
    x=load_img(file, target_size=(longitud,altura))
    x=img_to_array(x)
    x=np.expand_dims(x,axis=0)
    arreglo=cnn.Predict(x) #[[1,0,0]]
    resultado=arreglo[0] #[[0,0,1]]
    respuesta = np.argmax(resultado)
    if respuesta==0:
        print("gato")
    else:
         print("No es un gato")
    return respuesta

Predict('cat.jpg')
