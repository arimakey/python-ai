import cv2

def to_gray():
    image_path = input("Ingrese el nombre de la imagen (Debe encontrarse en la carpeta princpal) : ")

    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("original", image)
    cv2.imshow("gray", image_gray)
    cv2.waitKey()

to_gray()