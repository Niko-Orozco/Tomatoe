#!/usr/bin/env python3
import sys, os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

K.clear_session()
data_entrenamiento='./Data/Entrenamiento'
data_validacion ='./Data/Validacion'

#Parametros
epocas=20
altura, longitud= 100, 100
batch_size=32
pasos=1000
pasos_validacion=200
filtrosConv1=32
filtrosConv2=64
tamano_filtro1=(3,3)
tamano_filtro2=(2,2)
tamano_pool=(2,2)
clases = 1
lr=0.0005

#Pre Procesamiento de imagenes

entrenamiento_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True
)


validacion_datagen = ImageDataGenerator(
    rescale=1./255,
)


imagen_emtrenamiento = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)

imagen_validacion=validacion_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)


#Crear Cnn
cnn = Sequential()
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding='same', input_shape=(altura, longitud,3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu')) #Re ajustamos
cnn.add(Dropout(0.5))
cnn.add(Dense(clases,activation='softnax'))

cnn.compile(loss='categorical_crossentropy', optimize=optimizer.Adan(lr=lr), netrics=['accuracy'])
cnn.fit(imagen_emtrenamiento, steps_per_epoch=pasosm, epochs=epocas, validation_data=imagen_validacion, validation_steps=pasos_validacion)

dir = './model/'
if not os.path.exists(dir):
    os.mkdir(dir)
cnn.save('./model/models.cnt')
cnn.save_weights('./model/pesos.cnt')
