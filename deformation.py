import cv2
import numpy as np

def deformation():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta princpal) : ")
    image = cv2.imread(image_path)

    height, width = image.shape[:2]
    result = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            y_offset = int(20 * np.sin((j / width) * np.pi))  # Efecto cóncavo
            new_j = j
            new_i = i + y_offset

            if 0 <= new_i < height:
                result[new_i, new_j] = image[i, j]

    cv2.imshow('Imagen Original', image)
    cv2.imshow('Imagen Deformada', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

deformation()