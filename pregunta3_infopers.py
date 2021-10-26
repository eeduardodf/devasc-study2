while True :
        name = input("Hola, ¿Cuál es su nombre?\n")
        apellido = input("¿Cuales son sus apellidos?\n")
        edad = str(input("¿Cuantos años tiene? \n"))
        lugar = input("¿Cual es su lugar de residencia?\n")
        telef = str(input("¿Cuál es el número de su teléfono celular o fijo?\n"))
        carrera = input("¿Qué carrera esta estudiando?\n")
        print("Esta es la información que se ha recopilado:\n" + "Su nombre es "+name+" "+apellido+ 
        " tiene, "+edad+" años,"+" vive en "+lugar+
        " , su número de telefono es "+telef+" y estudia la carrera de "+carrera+".\n")
        while True :
            valor = input("¿La informacion mostrada es correcta?.Escriba si/(s) o no/(n) : ")
            if valor == 'si' or valor =='s' :
                break
            elif valor =='no' or valor=='n' :
                print ("Porfavor , vuelva a corregir sus datos.Gracias")
                break
            else :
                    while True: 
                        valor= input ("Opcion no válida porfavor.Escriba una opción correcta.\nLa información es correcta? si/s o no:")
                        if valor == 'si' or valor =='s' or valor=='no' or valor =='n':
                            break
                        else :
                            print("Porfavor corriga la informacion:")
                    break 
        if valor =='si' or valor=='s' :
            print("Se ha registrado la información correctamente. Gracias.")
            break
        

        

