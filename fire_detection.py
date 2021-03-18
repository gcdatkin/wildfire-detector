import numpy as np
from PIL import Image
import tensorflow as tf

def predict_fire(image_path):
    path_to_model = 'resources/fire_detector.h5'

    fire_detector = tf.keras.models.load_model(path_to_model)

    image = tf.expand_dims(
        tf.keras.preprocessing.image.smart_resize(
            tf.convert_to_tensor(
                np.array(
                    Image.open(image_path)
                )
            ), size=(224, 224)
        ), axis=0)

    prediction = fire_detector.predict(image)

    return int(prediction)
