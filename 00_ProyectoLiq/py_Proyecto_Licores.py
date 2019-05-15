## Crea un licor, devuelve un diccionario licor
import os
def addLicor():
    lic_brand = input('Marca: ') # Marca
    lic_price = input('Precio: ') # ´Precio
    lic_quant = input('Cantidad: ') # Cantidad de paquetes
    lic_type = input('D/I: ') # Nacional o importado
    
    licor = {
        'Brand':lic_brand,
        'Price': float(lic_price),
        'Cant': int(lic_quant),
        'D/I': lic_type
    }
    return licor

# retorna una lista de lineas con cada fila del archivo
def listarLineas():
    list_Liq = []
    try:
        file_liquors = open(path)
        all_lines = file_liquors.readlines()
        for line in all_lines:
          #  print(line)
            list_Liq.append(line)
        file_liquors.close()   
        #print (list_Liq)
        return list_Liq
    except:
        print('Error de lectura de archivo')

# Transforma una linea en un diccionario de datos
def lineToDicc(linea):
    line = linea.split(';')
    dicc_licor = {
        'Brand': line[0],
        'Price': float(line[1]),
        'Cant': int(line[2]),
        'D/I': line[3]
    }
    return dicc_licor

# Transforma un diccionario de datos en una linea de texto
def diccToLine(dic_licor):
    line = f"{dic_licor['Brand']};{dic_licor['Price']};{dic_licor['Cant']};{dic_licor['D/I']}"
    return line


# Transforma una lista de lineas en una lista de diccionarios construidos con cada fila
def listarDiccionarios(listaLineas):
    dicc_licores = []
    for line in listaLineas:
        licor = lineToDicc(line)
        dicc_licores.append(licor)
    return dicc_licores

# Busca un licor por marca, retorna su diccionario respectivo
def buscarLicor(brand):
    try:
        file_Liq = open(path)
        line_File = file_Liq.readlines()
        for line in line_File:
            dic_licor = lineToDicc(line)
            if dic_licor.get('Brand') == brand:
                #print (dic_licor)
                return dic_licor
    except:
        print('Error de lectura de archivo')
        
# Devuelve un boolean segun exista o no un licor
def existeLicor(brand):
    try:
        file_Liq = open(path)
        line_File = file_Liq.readlines()
        for line in line_File:
            dic_licor = lineToDicc(line)
            if dic_licor.get('Brand') == brand:
                #print (dic_licor)
                return True
    except:
        print('Error de lectura de archivo')

# Metodo para modificar un licor, desde la lista de diccionarios
def modificarLicor(opcion):
    ok = False
    while not ok:
        brand = input('Ingrese la marca: ')
        if existeLicor(brand) == True:
            lista_diccionarios = listarLineas() #lineas de archivo a lista de diccionarios
            listaDiccs = listarDiccionarios(lista_diccionarios) #lista de dicionarios
            dic_licorActual = buscarLicor(brand) # diccionario del licor buscado
            indice = listaDiccs.index(dic_licorActual) # indice del dicc
            ok = True
            if opcion == 1: # Cambiar marca
                new_brand = input('Nueva marca: ') # solicita nueva marca
                dic_licorNuevo = { # crea el nuevo diccionario
                'Brand':new_brand,
                'Price': dic_licorActual['Price'],
                'Cant': dic_licorActual['Cant'],
                'D/I': dic_licorActual['D/I']
                }
                dic_licorActual.update(dic_licorNuevo) # actualiza el diccionario

            elif opcion == 2: # Cambiar precio
                new_price = input('Nuevo precio: ') # solicita nueva marca
                dic_licorNuevo = { # crea el nuevo diccionario
                'Brand':dic_licorActual['Brand'],
                'Price': new_price,
                'Cant': dic_licorActual['Cant'],
                'D/I': dic_licorActual['D/I']
                }
                dic_licorActual.update(dic_licorNuevo) # actualiza el diccionario

            elif opcion == 3: # Cambiar cantidad
                new_stock = input('Nuevo stock: ') # solicita nueva marca
                dic_licorNuevo = { # crea el nuevo diccionario
                'Brand':dic_licorActual['Brand'],
                'Price': dic_licorActual['Price'],
                'Cant': new_stock,
                'D/I': dic_licorActual['D/I']
                }
                dic_licorActual.update(dic_licorNuevo) # actualiza el diccionario

            elif opcion == 4: # cambiar tipo
                new_type = input('Nuevo stock: ') # solicita nueva marca
                dic_licorNuevo = { # crea el nuevo diccionario
                'Brand':dic_licorActual['Brand'],
                'Price': dic_licorActual['Price'],
                'Cant': dic_licorActual['Cant'],
                'D/I': new_type
                }
                dic_licorActual.update(dic_licorNuevo) # actualiza el diccionario

            else:
                print ('opcion no valida')

            listaDiccs[indice] = dic_licorActual
            #print (listaDiccs)
            return listaDiccs # devuelve una lista de dicionarios
        else:
              print ('Licor ingresado no disponible')
                
# Escribiendo cambios al archivo desde una lista de diccionarios
def diccToFile(lista_diccs):
    try:
        # Vaciando archivo
        file_Liq = open(path,mode='w')
        file_Liq.write('')
        file_Liq.close()
        # Agregando licores al archivo
        file_Liq2 = open(path,mode='a')
        for diccs in lista_diccs:
            linea = diccToLine(diccs) # dicc a linea
            print(linea)
            file_Liq2.write(linea)
        file_Liq.close()
    except:
        print('Error de lectura de archivo')
       # print(listarLineas())
        
#Metodo para eliminar un licor
def borrarLicor():
    brand = input('Ingrese la marca: ')
    lista_diccionarios = listarLineas() #lineas de archivo a lista de diccionarios
    listaDiccs = listarDiccionarios(lista_diccionarios) #lista de dicionarios
    dic_licorActual = buscarLicor(brand) # diccionario del licor buscado
    listaDiccs.remove(dic_licorActual)
    print(listaDiccs)
    diccToFile(listaDiccs)
    
path = './liquors2.txt' # archivo

#Menu de opciones
opcion = 0
salir = False
carrito = [] # arreglo que guarda las compras del cliente
os.system("cls") #Limpia a pantalla
while not salir:
    print ("Liquors EPN\n")
    print ("1. Cliente")
    print ("2. Administracion")
    print ("3. Salir")
    try:
        opcion = int(input('Digite su opcion: '))
        if opcion == 1:
            import os
            os.system("cls")
            print ("Bienvenido !!")
            print ("1. Comprar")
            print ("2. Ver licores disponibles")
            print ("3. Regresar al Menu")
            salir2 = False
            while not salir2:
                try:
                    opc = int(input('Digite su opcion: '))
                    if opc == 1:
                        ok = False
                        while not ok:
                            brand = input('Nombre del licor: ')
                            if existeLicor(brand) == True: #valida si existe licor
                                licorA = buscarLicor(brand)
                                cant = input("Cantidad: ")
                                licorB = {
                                    'Brand':licorA.get('Brand'),
                                    'Price':licorA.get('Price'),
                                    'Cant':cant,
                                    'D/I':licorA.get('D/I')
                                }
                                carrito.append(licorB)
                                ok = True # fin de ciclo si todo va bien
                                print ("1. Añadir otro producto")
                                print ("2. Ver licores disponibles")
                                print ("3. Finalizar compra")
                            else:
                                print ('Licor ingresado no disponible')
                            #os.system("cls") #Limpia a pantalla
                            
                    elif opc == 2:
                        all_liquors = listarDiccionarios(listarLineas())
                        for lic in all_liquors:
                            fila_lic = f"Marca: {lic['Brand']}   Precio: {lic['Price']}   Importado o Domestico:{lic['D/I']}"
                            print (fila_lic)
                        print ("1. Comprar")
                        print ("3. Regresar al Menu")
                    elif opc == 3:
                        salir2 = True
                        os.system("cls") #Limpia a pantalla
                        print('\nDetalle de Compra:')
                        sumT = 0
                        for car in carrito:
                            for key in car.keys():
                                print(f"{key} : {car[key]}")
                            units= car.get('Price') * float(car.get('Cant'))
                            sumT+=units
                          #  print (car)
                        print(f'Valor total: ${sumT} Gracias por su compra!\n')
                    else:
                        print ("Introduce un numero entre 1 y 2")
                except ValueError:
                    print('Error, introduce un numero entero')
    
        elif opcion == 2:
            import os
            os.system("cls")
            print ("Administración de Licores")
            print ("1. Registrar Nuevo Licor")
            print ("2. Modificar Licor existente")
            print ("3. Mostrar todos los licores")
            print ("4. Dar de baja")
            print ("5. Regresar al Menu")
            salir3 = False
            while not salir3:
                try:
                    opc = int(input('Digite su opcion: '))
                    if opc == 1: # registrar nuevo licor
                        new_licor = addLicor() # agrega un licor, new_licor es un diccionrio
                        file_Liq = open(path,mode='a') # escribir al archivo
                        file_Liq.write(new_licor['Brand']+';'+str(new_licor['Price'])+';'+str(new_licor['Cant'])+';'+new_licor['D/I']+'\n');
                        file_Liq.close()
                        os.system("cls") #Limpia a pantalla
                        print ("1. Registrar Nuevo Licor")
                        print ("5. Regresar al Menu anterior")
                    elif opc == 2: # modifica licor
                        print ("1. Cambiar Marca")
                        print ("2. Cambiar Precio")
                        print ("3. Cambiar Stock")
                        print ("4. Cambiar Tipo")
                        opc2 = int(input('Digite su opcion: '))
                        if opc2 > 0 and opc2 < 5:
                            #modificarLicor(opc2)
                            diccToFile(modificarLicor(opc2))
                            print ("3. Revisar cambios")
                            print ("5. Regresar al Menu")
                            os.system("cls") #Limpia a pantalla
                            
                    elif opc == 3: # Muestra todos los licores
                        all_liquors = listarDiccionarios(listarLineas())
                        for lic in all_liquors:
                            fila_lic = f"Marca: {lic['Brand']}   Precio: {lic['Price']}   Stock: {lic['Cant']}  Importado o Domestico:{lic['D/I']}"
                            print (fila_lic)
                        print ("1. Registrar Nuevo Licor")
                        print ("2. Modificar Licor existente")
                        print ("4. Dar de baja")
                        print ("5. Regresar al Menu")
                        os.system("cls") #Limpia a pantalla
                    elif opc == 4:
                        #print ("Dar de baja a Licor")
                        borrarLicor()
                        print ("3. Revisar cambios")
                        print ("5. Regresar al Menu")
                        os.system("cls") #Limpia a pantalla
                    elif opc == 5:
                        salir3 = True
                    else:
                        print ("Introduce un numero entre 1 y 5")
                except ValueError:
                    print('Error, introduce un numero entero')
            
        elif opcion == 3:
            os.system("cls") #Limpia a pantalla
            salir = True
        else:
            print ("Introduce un numero entre 1 y 3")
    except ValueError:
        print('Error, introduce un numero entero')
print ("Fin")
os.system("cls") #Limpia a pantalla