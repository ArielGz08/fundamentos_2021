print ("Se solicita ingresar sus datos para generar clave")
nombre = input("Introduce nombre:  ")
apellido = input("Introduce apellido:  ")
print ("ingrese fecha de nacimiento")
dia_nac = input("Introduce dia nac:  ")
mes_nac = input("Introduce mes nac:  ")
año_nac = input("Introduce año nac:  ")
fecha_nac= (dia_nac+"/"+ mes_nac+"/"+ año_nac)
print ("fecha ingresada:",fecha_nac)
clave= nombre[0]+apellido[0]+"_"+año_nac
print ("su clave es:",clave)
