ruta = "datosok.txt"   
with open(ruta, mode = "a", encoding = "utf-8") as fichero: 

    for i in range(10):
        print("1. Registrar un nombre. \n2. Buscar datos. \n3. Salir.")
        Caso = input()  
        if Caso == "1" :
            
                print("Escriba su cedula: ")
                Cedula = input()
                print("Escriba su nombre: ")
                Nombre = input()
                print("Escriba sus apellidos: ")
                Apellidos = input()
                print("Escriba su Edad: ")
                Edad = input()
                print("Desea guardar sus datos? Y/N")
                Guardar = input()
                
                if Guardar == "Y":
                    fichero.write("Cedula   ")
                    fichero.write("Nombres   ")
                    fichero.write("Apellidos   ")
                    fichero.write("Edad   ")
                    fichero.write("\n")
                    fichero.write(Cedula)
                    fichero.write("   ,")
                    fichero.write(Nombre)
                    fichero.write("   ,")
                    fichero.write(Apellidos)
                    fichero.write("   ,")
                    fichero.write(Edad)
                    fichero.write("\n")
                    fichero.write("\n")                    
                    print("Guardado!. Desea guardar mas datos?")
                    print("Y/N?")
                    Otra = input()                    
                    if Otra == "Y":    
                        i = 0
                    else:
                        i = 0
                    
                else:
                    print("Salio Correctamente.")
                    i = 0
        elif Caso == "2" :
            print("Escriba el dato que desea buscar:")
            Dato = input()           
            archivo = open("datosok.txt", "r")             
            flag = 0
            index = 0            
            for line in archivo:  
                index += 1                 
                if Dato in line:                  
                  flag = 1
                  break                      
            if flag == 0: 
               print('El dato: ', Dato , 'no se encontro.') 
            else: 
               print('El dato: ', Dato, 'Se encontro en la linea', index,'\n', line)  
            archivo.close()
        
        elif Caso == "3":
            break
        
            
            
