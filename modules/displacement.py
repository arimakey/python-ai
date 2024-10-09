import cv2
import numpy as np

def displacement():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta princpal) : ")

    displacement_x = 100
    displacement_y = 100

    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    M = np.float32([[1, 0, displacement_x], [0, 1, displacement_y]])

    displacement_image = cv2.warpAffine(image, M, (width, height))

    cv2.imshow("Original", image)
    cv2.imshow("Trasladada", displacement_image)

    cv2.waitKey()

displacement()