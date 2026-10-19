import matplotlib.pyplot as ptl 
import numpy as np

def f(x):
    return 320*x 

def g(x):
    return 260*x+180

X = np.linspace(0,11,11)

Y = f(X) 
C = g(X)

ptl.plot(X,Y, label='sitio de internet 1', color ='r', marker ="*")
ptl.plot(X,C, label="sitio de internet 2", color ='b', marker ='+')

ptl.title("Comparación de precios de distintos sitos de internet")
ptl.xlabel("Tablets comprados")
ptl.ylabel("Costo total (en dólares) ")
ptl.legend("")
ptl.grid(True)
ptl.show()

print("A continuación del código, responda la siguiente pregunta: ¿Desde cuántas tablets (unidades), el cobro es más conveniente en el sitio de internet 2 que en el sitio 1?")
print("Apartir de la comprar numero 4 es mejor el sitio de internet 2")