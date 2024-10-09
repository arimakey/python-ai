import cv2
import numpy as np

def blur():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta princpal) : ")
    image = cv2.imread(image_path)

    height, width = image.shape[:2]
    kernel_gaussian = np.array([[1/16, 1/8, 1/16],
                   [1/8,  1/4,  1/8],
                   [1/16, 1/8,  1/16]])

    kernel_simple = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])


    blurred_image = cv2.filter2D(image, -1, kernel_simple)
    gaussian_image = cv2.filter2D(image, -1, kernel_gaussian)


    cv2.imshow('Imagen Original', image)
    cv2.imshow('Difumidado simple', blurred_image)
    cv2.imshow('Difuminado gaussiano', gaussian_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

blur()