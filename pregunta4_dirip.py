

#IDENTIFICACIÓN IP PUBLICA O PRIVADA

print("Coloque la dirección IP , sin puntos: \n")

o1= int(input("Valor del 1er octeto : "));o2=int(input("Valor del 2do octeto : "));o3=int(input("Valor del 3er octeto : "));o4=int(input("Valor del 4to octeto : "))

print("La dirección ip introducida es: " , end="")
print(o1,end=".")
print(o2,end=".")
print(o3,end=".")
print(o4)
ipadd = [o1,o2,o3,o4]
if ipadd[0] == 10 and ipadd[1]>=0 and ipadd[1]<=255 and ipadd[2]>=0 and ipadd[2]<=255 and ipadd[3]>=0 and ipadd[3]<=255 :
    print ("Esta es una dirección privada")
elif ipadd[0] == 172 and ipadd[1]>=16 and ipadd[1]<=31 and ipadd[2]>=0 and ipadd[2]<=255 and ipadd[3]>=0 and ipadd[3]<=255 :
    print ("Esta es una dirección privada")
elif ipadd[0] ==192 and ipadd[1]==168 and ipadd[2]>=0 and ipadd[2]<=255 and ipadd[3]>=0 and ipadd[3]<=255 :
    print ("Esta es una direccion privada")
elif ipadd[0]>=256 or ipadd[1]>=256 or ipadd[2]>=256 or ipadd[3]>=256 :
    print("Esta dirección IP no es válida.")
else :
    print("Esta es una dirrección pública.")

#IDENTIFICACIÓN IP CLASE A , B ,C ,D ,E:
if ipadd[0] > 0 and ipadd[0] <= 127 and ipadd[1]>=0 and ipadd[1]<=255 and ipadd[2]>=0 and ipadd[2]<=255 and ipadd[3]>0 and ipadd[3]<=255:
        print("Es de clase : A")
elif ipadd[0] >= 128 and ipadd[0] <= 191 and ipadd[1]>=0 and ipadd[1]<=255 and ipadd[2]>=0 and ipadd[2]<=255 and ipadd[3]>0 and ipadd[3]<=255:
        print("Es de clase : B")
elif ipadd[0] >= 192 and ipadd[0] <= 223 and ipadd[1]>=0 and ipadd[1]<=255 and ipadd[2]>=0 and ipadd[2]<=255 and ipadd[3]>0 and ipadd[3]<=255:
        print("Es de clase : C")
elif ipadd[0] >= 224 and ipadd[0] <= 239 and ipadd[1]>=0 and ipadd[1]<=255 and ipadd[2]>=0 and ipadd[2]<=255 and ipadd[3]>0 and ipadd[3]<=255:
        print("Es de clase : D")
elif ipadd[0] >= 240 and ipadd[0] <= 247 and ipadd[1]>=0 and ipadd[1]<=255 and ipadd[2]>=0 and ipadd[2]<=255 and ipadd[3]>0 and ipadd[3]<=255:
        print("Es de clase : E")
else :
    ipadd[0] > 255
    print("No se puede identificar a que clase pertenece porque la dirección IP no es válida.")
