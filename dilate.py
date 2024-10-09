import numpy as np
import cv2

def dilate():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta princpal) : ")

    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    kernel = np.ones((5,5), np.uint8)

    dilation = cv2.dilate(image, kernel, iterations=1)

    cv2.imshow("Imagen Original", image)
    cv2.imshow("Imagen con Perspectiva", dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
dilate()