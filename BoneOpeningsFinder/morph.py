from skimage import io

from BoneOpeningsFinder.morph_mask import MorphMasker
from BoneOpeningsFinder.morph_opening import MorphOpening

opening = MorphOpening()
masker = MorphMasker()


def predict(xray_path):
    """Detect leg-bone on xRay photo and create morphology opening transformation"""
    image = io.imread(xray_path)
    predicted_image_path = f'{xray_path[:-4]}_prediction.png'
    masked_image_path = f'{xray_path[:-4]}_mask.png'
    predicted_opening = opening.predict(image, predicted_image_path)
    masker.mask(predicted_opening, image, masked_image_path)
    return predicted_image_path, masked_image_path
