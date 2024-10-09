import cv2
import numpy as np

def edge_detection():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta principal): ")
    image = cv2.imread(image_path)


    edge_image = cv2.Canny(image, 50, 200)

    cv2.imshow('Imagen Original', image)
    cv2.imshow('Imagen de bordes', edge_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

edge_detection()
