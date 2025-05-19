nombres = ["agustina", "brenda", "hernan","marcele","franco", "marcela"]
edades =[9,40, 30,20,10,22]
generos =["F", "F", "M", "X", "M", "X"]

def mostrar_datos(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(len(lista_a)):

        if len(lista_a[i]) < 8:
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}")
        else:
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}")    

def copiar_lista(lista_a:list, lista_b:list)->list:
    nombres_originales = [-1] * len(lista_a)
    edades_originales = [-1] * len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i] = lista_a[i]
        edades_originales[i] = lista_b[i]
    
    return nombres_originales, edades_originales

def funcion_orden_ascendente(lista_a:list, lista_b:list, lista_c:list) -> list:

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if lista_c[i] > lista_c[j]:
            
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] > lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

mostrar_datos(generos,edades,nombres)
print("\n")
funcion_orden_ascendente(edades,generos,nombres)
print("\n")
mostrar_datos(generos,edades,nombres)


def verificar_cadena_numeros(cadena:str) -> bool:
    verificacion = False

    for i in cadena:
        if (48 < ord(i) < 57 ):
            verificacion = True

    return verificacion



def verificar_correo_electronico (cadena:str) -> bool:
    verificacion_arroba = False
    contador_arrobas = 0
    posicion_arroba = None
    verificacion_punto = False

    for i in cadena:
        if (64 == ord(i)):
            contador_arrobas = contador_arrobas + 1
            verificacion_arroba = True 
            for o in range(len(cadena)):
                if (cadena[o] == i):
                    posicion_arroba = o
       
    if (verificacion_arroba == True and contador_arrobas == 1):
        for a in range(posicion_arroba, len(cadena) ,1):
            if (46 == ord(cadena[a])):
                verificacion_punto = True

    return verificacion_punto





    
   


