import numpy as np
from skimage import img_as_ubyte
from skimage import io
from skimage import morphology, color


class MorphMasker:

    def mask(self, opening_prediction, image, save_path):
        opening_mask = opening_prediction > 0.5
        mask_img = self.mask_image(image, opening_mask, alpha=0.5)
        io.imsave(save_path, img_as_ubyte(mask_img))
        return save_path

    def mask_image(self, image, opening_mask, alpha=1.0):
        """Based on prediction, apply overlay red stroke and blue fill on given XRay image"""
        rows, cols = image.shape
        color_mask = np.zeros((rows, cols, 3))

        boundary = morphology.dilation(opening_mask, morphology.disk(2)) ^ opening_mask

        color_mask[opening_mask == 1] = [0, 0, 1]
        color_mask[boundary == 1] = [1, 0, 0]
        img_color = np.dstack((image, image, image))

        img_hsv = color.rgb2hsv(img_color)
        color_mask_hsv = color.rgb2hsv(color_mask)

        img_hsv[..., 0] = color_mask_hsv[..., 0]
        img_hsv[..., 1] = color_mask_hsv[..., 1] * alpha

        img_masked = color.hsv2rgb(img_hsv)
        return img_masked
