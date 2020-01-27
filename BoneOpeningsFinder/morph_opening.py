import numpy as np
import tensorflow as tf
from keras.models import model_from_json
from skimage import img_as_ubyte
from skimage import morphology
from skimage import transform, io

tf_graph = tf.get_default_graph()


class MorphOpening:

    def __init__(self):
        with open('ml_model/model_bk.json', 'r') as raw_model:
            loaded_model = model_from_json(raw_model.read())
        loaded_model.load_weights('ml_model/trained_model.hdf5')
        self.model = loaded_model

    def predict(self, image, predicted_image_path):
        """Returns predicted morphology opening on leg bones using pre-trained BK model"""
        transformed_image = self._transform_image(image)
        with tf_graph.as_default():
            prediction = self.model.predict(transformed_image)[..., 0].reshape(*image.shape)
        prediction = prediction > 0.5
        predicted_opening = morphology.opening(img_as_ubyte(prediction))
        io.imsave(predicted_image_path, predicted_opening)

        return predicted_opening

    def _transform_image(self, image):
        """Transform image for prediction (add 2 dimensions and do mean with std)"""
        tr_image = transform.resize(image, (512, 256), mode='constant')
        tr_image = np.expand_dims(tr_image, -1)
        tr_image = tr_image[None, ...]

        tr_image -= tr_image.mean()
        tr_image /= tr_image.std()

        return tr_image
