import cv2
import numpy as np

def scale():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta princpal) : ")
    scale_x = 0.5
    scale_y = 0.5

    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    M = np.float32([[scale_x, 0, 0], [0, scale_y, 0]])

    scale_image = cv2.warpAffine(image, M, (int(width * scale_x), int(height * scale_y)))

    cv2.imshow("Imagen Original", image)
    cv2.imshow("Imagen escalada", scale_image)
    cv2.waitKey()


scale()


