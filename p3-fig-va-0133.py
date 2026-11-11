import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Karla Saenz NC 0133
print("Karla Saenz NC 0133")
print("Ull aCT3 COLOCAR PUNTOS A UNA IMAGEN EN  BANCO Y NEGRO Karla Saenz NC 0133")
nombre_imagen = "Vicentefernandes-0133.jpg"
img_bgr = cv2.imread(nombre_imagen)
if img_bgr is None:
    print(
        f"Error: No se pudo encontrar o cargar la imagen '{nombre_imagen}'. Asegúrate de que esté en la misma carpeta."
    )
else:
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    plt.imshow(img_gris, cmap="gray")
    plt.title("VicenteFernandes y Karla Saenz 0133")
    plt.axis("on") 
    plt.show()
    print("-+-+-+- Puntos en la imagen-+-+--++")
    plt.imshow(img_gris, cmap="gray")
    X = [100, 100, 300]
    Y = [100, 400, 500]
    plt.scatter(X, Y, s=50, c="pink", edgecolors="black")
    plt.title("Puntos sobre la imagen Karla Saenz nc 0133")
    plt.show()
    print("-+-+-+-+-+- cuadro azul en la imagen-+-+-+-")
    plt.imshow(img_rgb)  
# Definición de coordenadas (X, Y) para formar el cuadro cerrado
x = [200, 500, 500, 200, 200]
y = [250, 250, 500, 500, 250]
plt.imshow(img_rgb)
plt.plot(x, y, c="blue", linewidth=2)
plt.title("Cuadro azul sobre la imagen")
plt.show()
# Nuevas coordenadas del cuadro
x = [160, 160, 460, 460, 160]
y = [450, 150, 150, 450, 450]
plt.imshow(img_rgb)
plt.plot(x, y, c="blue", linewidth=2)
plt.title("Cuadro azul sobre la imagen Karla Saenz NC 0133")
plt.show()
print("-+-+-+- circulo verde en la imagen -+--+-+-++-+-")
I = cv2.imread("Vicentefernandes-0133.jpg")
plt.imshow(I)
N = 30 # LADOS DE POLIGONO
X = np.zeros((N+1,))
Y = np.zeros((N+1,))
(xc,yc) = (340,320)
r = 150 # radio
for i in range(N+1):
T = 2*np.pi/N*i
X[i] = xc + r*np.cos(T)
y[i] = yc + T*np.sin(T)
plt.plot(x,y,c="green")
plt.show()