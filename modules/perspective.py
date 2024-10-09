import numpy as np
import cv2

def perspective():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta princpal) : ")

    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    origin = np.float32([[0, 0], [width - 1, 0], [0, height], [width - 1, height]])
    destiny = np.float32([[10, 100], [width - 10, 50], [50, height - 50], [width - 50, height - 10]])

    M = cv2.getPerspectiveTransform(origin, destiny)


    transformed_image = cv2.warpPerspective(image, M, (width, height))


    cv2.imshow("Imagen Original", image)
    cv2.imshow("Imagen con Perspectiva", transformed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
perspective()