import numpy as np
from keras.utils import load_img, img_to_array
from keras.models import load_model

longitud, altura = 100, 100
modelo = './modelo/modelo.h5'
pesos = './modelo/pesos.h5'

cnn = load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
    x = load_img(file, target_size = (longitud, altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    arreglo = cnn.predict(x)    # [ [1, 0, 0] ] -> 2D
    resultado = arreglo[0]      # [1, 0, 0]
    respuesta = np.argmax(resultado)    # 0 -> arr[0] tiene el valor más alto

    if respuesta == 0:
        print('Melanoma')
    elif respuesta == 1:
        print('Carcinoma de células basales')
    elif respuesta == 5:
        print('Nevus melanocíticos')
    elif respuesta == 6:
        print('Lesion vascular de la piel')
    return respuesta




# #
# Manejo de epoca / paso.

# model.load_weights('modelo.h5')

# val_loss, val_cat_acc, val_top_2_acc, val_top_3_acc = \
# model.evaluate_generator(test_batches, 
#                         steps=len(df_val))

# print('val_loss:', val_loss)
# print('val_cat_acc:', val_cat_acc)
# print('val_top_2_acc:', val_top_2_acc)
# print('val_top_3_acc:', val_top_3_acc)


#   Prediction

predict('xx.jpg')