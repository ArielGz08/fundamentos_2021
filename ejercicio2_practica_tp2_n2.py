import math
print ("Ingresar largo y ancho para calculo de paneles de pasto")
print ("los paneles son de 0.60x0.60m. Ingrese medidas del espacio a cubrir")
ancho = float (input("Introduce ancho ml:  "))
largo = float (input("Introduce largo ml:  "))
sup_de_terreno= ancho*largo
print ("superficie de terreno m2: ", sup_de_terreno)
panel_ancho = 0.60
panel_largo= 0.60
sup_de_panel= (panel_ancho*panel_largo)
print ("superficie por panel m2:",sup_de_panel)
cantidad_panel= (sup_de_terreno/sup_de_panel)
print ("cantidad_panel:",cantidad_panel)
math.ceil(cantidad_panel)
print(str(math.ceil(cantidad_panel)) + (" unidades es la cantidad de panel a utilizar"))
