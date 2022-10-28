import numpy as np
from skimage.color import rgb7gray
from skimage.exposure import match_histograms
from skimage.metric import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Especifique 2 imagens com a mesma forma."
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full = True)
    print("Semelhança das imagens:", score)
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_difference_image

def transfer_histogram(image1, image2)
    matched_image = match_histograms(image1, image2, mutichannel=True)
    return matched_image