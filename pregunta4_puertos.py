#IDENTIFICAR PUERTOS LÓGICOS
puerto = int(input("Ingrese un número de puerto para identificar el tipo de puerto desde [1-65535] : \n"))
if puerto > 0 and puerto <= 1023 :
    print("Este es un puerto bien conocido.")
elif puerto > 1024 and puerto <=49151 :
    print ("Este es un puerto registrado.")
elif puerto > 49152 and puerto <= 65535 :
    print("Este es un puerto privado.")
else:
    print("Este número de puerto no es válido.")


 
