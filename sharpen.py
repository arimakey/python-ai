import cv2
import numpy as np

def sharpen():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta principal): ")
    image = cv2.imread(image_path)

    kernel_sharpen = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])

    sharpened_image = cv2.filter2D(image, -1, kernel_sharpen)

    cv2.imshow('Imagen Original', image)
    cv2.imshow('Imagen Enfocada', sharpened_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

sharpen()
