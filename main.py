import numpy as np  # performance stuff
import cv2 as cv  # opencv
import os  # debug levels
import matplotlib.pyplot as plt
import matplotlib


def extractClothShape(cloth):
    pass


def resizeImage(sourceShape, destinationShape):
    pass


def replaceClothesRegion(sourceShape, destinationShape):
    pass

# Pseudocode:
# cloth1 = image(file1)
# cloth2 = image(file2)
#
# clothShape1 = extractClothShape(cloth1)
# clothShape2 = extractClothShape(cloth2)
#
# resizedClothRegion2 = resizeImage(clothShape2, clothShape1)
#
# swappedImage = replaceClothesRegion(cloth1, resizedClothRegion2)
#
# return swappedImage

# Sources:
# https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/
# https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html
# https://learnopencv.com/image-segmentation/
# https://www.opencvhelp.org/tutorials/image-analysis/image-segmentation/
# https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html


def main():
    # matplotlib backend. doesn't properly work on wayland
    matplotlib.use('TkAgg')
    debug = int(os.environ['DEBUG'])  # was taken from tinygrad
    # sample_image = cv2.imread('human.jpg')
    # img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)
    # plt.imshow(img)
    # plt.show(sample_image)
    img = cv.imread('human.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    same_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    ret, thresh = cv.threshold(gray, 0, 255,
                               cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    if debug == 1:
        grid = plt.figure(figsize=(10, 7))
        grid.add_subplot(2, 2, 1)
        plt.imshow(img)
        plt.axis('off')
        plt.title('img')
        grid.add_subplot(2, 2, 2)
        plt.imshow(gray)
        plt.axis('off')
        plt.title('gray')
        grid.add_subplot(2, 2, 3)
        plt.imshow(same_img)
        plt.axis('off')
        plt.title('same_img')
        plt.show()


main()
