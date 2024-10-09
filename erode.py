import numpy as np
import cv2

def erode():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta princpal) : ")

    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    kernel = np.ones((5,5), np.uint8)

    erosion = cv2.erode(image, kernel, iterations=1)

    cv2.imshow("Imagen Original", image)
    cv2.imshow("Imagen con Perspectiva", erosion)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
erode()