def mensaje_home() -> str:
    """

    Mensaje de consola del home

    """

    return ("\n<<<<<<<<<<->>>>>>>>>>\nBienvenido EduSystem - Home\n\n1-Cargar datos de alumnos.\n2-Mostrar datos de alumnos.\n3-Calcular promedio de notas.\n4-Mostrar promedio de manera DESCENDENTE o ASCENDENTE.\n5-Mayor promedio de materia.\n6-Buscar por legajo.\n7-Calificacion por materia repetida.\n8-Salir del programa\n<<<<<<<<<<->>>>>>>>>>\n")

def mensaje_ingresar_nombre_alumno(i:int) -> str:
    """
    
    Mensaje de consola para solicitar nombre de alumno.

    """
    return (f"Ingrese el nombre del alumno n°{i+1}: ")

def mensaje_ingresar_genero_alumno(i:int) -> str:
    """
    
    Mensaje de consola para solicitar genero de alumno.

    """
    return (f"Ingrese el genero del alumno {i} (M-F-X): ")

def mensaje_ingresar_legajo_alumno(i:int) -> str:
    """
    
    Mensaje de consola para solicitar legajo de alumno.

    """
    return (f"Ingrese el numero de legajo del alumno {i} (5 numeros): ")

def mensaje_ingresar_nota_alumno(i:int, x:int, ) -> str:
    """
    
    Mensaje de consola para solicitar notas de alumno.

    """
    return (f"Ingrese el nota de la materia n°{x+1} del alumno {i}: ")

def mensaje_mostrar_alumno() -> str:
    """
    
    Mensaje de consola para solicitar numero de legajo de alumno.

    """
    return("Ingrese un numero de legajo existente:")



def validar_home() -> str:
    """
    Solicita y valida los datos ingresados por el usuario en el "Home".
    
    Args:
    Ninguno.

    Returns:
    Devuelve si el valor fue "1","2","3" o "4"

    """
    
    validacion = True
    opcion = input(mensaje_home())

    while (validacion):

        if (opcion is None):
            
            opcion = input(mensaje_home())

        else:
            if (opcion == "1"):
                validacion = False
            elif (opcion == "2"):
                validacion = False
            elif (opcion == "3"):
                validacion = False
            elif (opcion == "4"):
                validacion = False
            elif (opcion == "5"):
                validacion = False
            elif (opcion == "6"):
                validacion = False
            elif (opcion == "7"):
                validacion = False
            elif (opcion == "8"):
                validacion = False
            else:
                opcion = input(mensaje_home())
        
    return opcion

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial=0) -> list:
    

    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]

    return matriz


def cargar_alumnos(nombres_estudiantes:list,  generos_estudiantes:list, legajos:list, notas_materias:list) -> str:
    
    """
    Solicita, valida y carga los datos de los alumnos como nombres, generos, legajos y materias en una matriz.
    
    Args:
    nombre_estudiantes: Lista donde se cargaran los nombres de los alumnos despues de ser solicitados y validados.
    
    generos_estudiantes: Lista donde se cargaran los generos posibles (M, F y X) de los alumnos despues de ser solicitados y validados.

    notas_materias: Matriz donde se cargaran las posibles notas (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) de los alumnos despues de ser solicitados y validados. (Columnas = Materias / Filas = Alumnos)

    Returns:
    Una vez que terminar de solicitar, validar y cargar los datos de cada alumnos retornara un mensaje "Los 30 alumnos fueron cargados correctamente!".

    """
    
    cantidad_alumnos = len(nombres_estudiantes)
    validacion_nombre = True
    
    for i in range(0, cantidad_alumnos, 1):
        validacion_nombre = True
        while (validacion_nombre):
            nombre = input(mensaje_ingresar_nombre_alumno(i))
            for o in (nombre):
                if (65 <= ord(o) <= 90 or 97 <= ord(o) <= 122):
                    validacion_nombre = False    
                else:
                    validacion_nombre = True
                    break        
        
        nombres_estudiantes[i] = nombre 

        validacion_genero = True
        while (validacion_genero):
            genero = input(mensaje_ingresar_genero_alumno(nombres_estudiantes[i]))
            if (genero == "M"):
                validacion_genero = False
            elif (genero == "F"):
                validacion_genero = False   
            elif (genero == "X"):
                validacion_genero = False         
            else:
                validacion_genero = True 
        
        generos_estudiantes[i] = genero
        
        validacion_legajo = True
        while (validacion_legajo):
            numero_legajo = input(mensaje_ingresar_legajo_alumno(nombres_estudiantes[i]))
            for o in (numero_legajo):
                cantidad = len(numero_legajo)
                if (cantidad == 5):
                    if (48 <= ord(o) <=57):
                        validacion_legajo = False    
                    else:
                        validacion_legajo = True
                        break     

        legajos[i] = numero_legajo

        for x in range(5):
            validacion = True
            while (validacion):
                nota = input(mensaje_ingresar_nota_alumno(nombres_estudiantes[i],x))
                if (nota is None):
                    validacion = True
                else:
                    if(nota == "1"):
                        validacion = False
                    elif(nota == "2"):
                        validacion = False 
                    elif(nota == "3"):
                        validacion = False 
                    elif(nota == "4"):
                        validacion = False 
                    elif(nota == "5"):
                        validacion = False 
                    elif(nota == "6"):
                        validacion = False 
                    elif(nota == "7"):
                        validacion = False 
                    elif(nota == "8"):
                        validacion = False 
                    elif(nota == "9"):
                        validacion = False 
                    elif(nota == "10"):
                        validacion = False 
                    else:
                        validacion = True
                      
            notas_materias[i][x] = int(nota)   
                

    return ("Los 30 alumnos fueron cargados correctamente!")      
              
        
def mostrar_un_alumno(legajos: list, generos_estudiantes: list, notas_materias: list, nombres_estudiantes: list) -> str:
    
    """
    Recibe las lista de legajos, matriz notas_materias y lista nombres_estudiantes para enviar por una funcion un indice que corresponde a un alumno (legajos).
    
    Args:
    legajos: Lista donde estan cargados los legajos de los alumnos.
    
    generos_estudiantes: Lista donde estan cargados los generos de los alumnos.

    notas_materias: Matriz donde estan cargadas las notas de los alumnos.

    nombres_estudiantes: Lista donde estan cargados los nombres de los alumnos.

    Returns:
    Una vez que terminar de enviar todos los indices de la lista legajos y las listas retorna el mensaje "Los 30 alumnos fueron mostrados correctamente!".

    """
    
    for i in range(len(legajos)):
        mostrar_datos_alumno(i, legajos, generos_estudiantes, notas_materias, nombres_estudiantes)

    return ("Los 30 alumnos fueron mostrados correctamente!")
        

def mostrar_datos_alumno(indice_legajo: int, legajos: list, generos_estudiantes: list, notas_materias: list, nombres_estudiantes: list):
    
    """
    Recibe indice de un legajo, matriz notas_materias y lista nombres_estudiantes para ser imprimido en consola.
    
    Args:
    indice_legajo: Indice del alumno que se usara para imprimir las lista.

    legajos: Lista donde estan cargados los legajos de los alumnos.
    
    generos_estudiantes: Lista donde estan cargados los generos de los alumnos.

    notas_materias: Matriz donde estan cargadas las notas de los alumnos.

    nombres_estudiantes: Lista donde estan cargados los nombres de los alumnos.

    Returns:
    

    """
    
    mensaje = (
       
        f"Datos del alumno:\n"
        f"Legajo: {legajos[indice_legajo]}\n"
        f"Nombre: {nombres_estudiantes[indice_legajo]}\n"
        f"Género: {generos_estudiantes[indice_legajo]}\n"
        f"Materia_1\tMateria_2\tMateria_3\tMateria_4\tMateria_5\n"
        f"{notas_materias[indice_legajo][0]}\t\t"
        f"{notas_materias[indice_legajo][1]}\t\t"
        f"{notas_materias[indice_legajo][2]}\t\t"
        f"{notas_materias[indice_legajo][3]}\t\t"
        f"{notas_materias[indice_legajo][4]}\n"

    )
    print(mensaje)
    

def buscar_alumno_legajo_promedio(legajos:list, generos_estudiantes:list, notas_materias:list, nombres_estudiantes:list, promedios_alumnos:list) -> str:
    
    """
    Solicita y valida un numero de legajo de un alumno para obtener el indice en la lista legajo para luego guardarlo en la variable posicion y 
    enviarlo a una funcion junto a las listas legajos, generos_estudiantes, notas_materias, nombres_estudiantes, promedios_alumnos.
    
    Args:
    legajos: Lista donde estan cargados los legajos de los alumnos.
    
    generos_estudiantes: Lista donde estan cargados los generos de los alumnos.

    notas_materias: Matriz donde estan cargadas las notas de los alumnos.

    nombres_estudiantes: Lista donde estan cargados los nombres de los alumnos.

    promedios_alumnos: Lista donde estan cargados los promedios de los alumnos.

    Returns:
    Una vez que termine de enviar los datos a la funcion retornara un mensaje "El alumnos fue mostrado correctamente!".

    """
    
    validacion = True
    posicion = None
    validacion_legajo = True

    while(validacion_legajo):

        while (validacion):
            legajo = input(mensaje_mostrar_alumno())    
            if (legajo is None):
                legajo = input(mensaje_mostrar_alumno())
            else:
                if (len(legajo) == 5):
                    for x in (legajo):
                        if (48 <= ord(x) <= 57):
                            validacion = False
                        else:
                            validacion = True
                            break
                

            
        if (validacion == False):
            posicion = len(legajos)
            for i in range(posicion):
                if (legajos[i] == int(legajo)):
                    validacion = False
                    posicion = i
                    validacion_legajo = False
                    break
            
            if (validacion_legajo==True):
                return("No existe este legajo\n")

            
    
    mostrar_alumno_legajo_promedio(legajos, generos_estudiantes, notas_materias, nombres_estudiantes, promedios_alumnos, posicion)

    return ("El alumnos fue mostrado correctamente!")
 

def mostrar_alumno_legajo_promedio(legajos:list, generos_estudiantes:list, notas_materias:list, nombres_estudiantes:list, promedios_alumnos:list, posicion:int) -> str:
    
    """
    Recibe la "posicion" de un legajo la lista legajos, matriz notas_materias, lista promedios_alumnos y lista nombres_estudiantes para ser imprimido en consola.
    
    Args:
    indice_legajo: Indice del alumno que se usara para imprimir las lista.

    legajos: Lista donde estan cargados los legajos de los alumnos.
    
    generos_estudiantes: Lista donde estan cargados los generos de los alumnos.

    notas_materias: Matriz donde estan cargadas las notas de los alumnos.

    nombres_estudiantes: Lista donde estan cargados los nombres de los alumnos.

    posicion: El valor que se usara como indice para todas las listas.

    Returns:

    """
    
    mensaje =  (
    f"\nDatos del alumno:\n"
    f"Legajo: {legajos[posicion]}\n"
    f"Nombre: {nombres_estudiantes[posicion]}\n"
    f"Género: {generos_estudiantes[posicion]}\n"
    "Materia_1\tMateria_2\tMateria_3\tMateria_4\tMateria_5\n"
    f"{notas_materias[posicion][0]}\t\t"
    f"{notas_materias[posicion][1]}\t\t"
    f"{notas_materias[posicion][2]}\t\t"
    f"{notas_materias[posicion][3]}\t\t"
    f"{notas_materias[posicion][4]}\n"
    f"Promedio de notas: {promedios_alumnos[posicion]}"
    )

    print(mensaje)


def calcular_promedios (nombres_estudiantes:list, promedios_alumnos:list, notas_materias:list)-> str:

    """
    Calcula los promedios de los alumnos y luego las cargas en la lista promedios por indice.
    
    Args:
    
    notas_materias: Matriz donde estan cargadas las notas de los alumnos.

    nombres_estudiantes: Lista donde estan cargados los nombres de los alumnos.

    promedios_alumnos: Lista para cargar los promedio segun su indice.

    Returns:
    Retorna un mensaje "Todos los alumnos fueron mostrados promediados.".

    """
    
    cantidad_alumnos = len(nombres_estudiantes)
    
    for i in range(cantidad_alumnos):
        promedio = (notas_materias[i][0] + notas_materias[i][1] + notas_materias[i][2] + notas_materias[i][3] + notas_materias[i][4]) / 5
        promedios_alumnos[i] = promedio  

    return "Todos los alumnos fueron mostrados promediados."


def mostrar_todos_alumnos_promedio(legajos:list, generos_estudiantes:list, notas_materias:list, nombres_estudiantes:list, promedios_alumnos:list) -> str:
    
    """
    Calcula los promedios de los alumnos por medio de una funcion, solicita y valida como ordenar los alumnos de forma ascendente o decendente para
    luego muestra los datos de los alumnos junto a sus promedios en consola.
    
    Args:
    
    legajos: Lista donde estan cargados los legajos de los alumnos.
    
    generos_estudiantes: Lista donde estan cargados los generos de los alumnos.

    notas_materias: Matriz donde estan cargadas las notas de los alumnos.

    nombres_estudiantes: Lista donde estan cargados los nombres de los alumnos.

    promedios_alumnos: Lista donde estan cargados los promedios de los alumnos.

    Returns:
    Retorna un mensaje "Todos los alumnos fueron mostrados correctamente."

    """
    

    calcular_promedios(nombres_estudiantes,promedios_alumnos,notas_materias)
    

    posicion = len(legajos)
    verificacion_condicion = True
    while (verificacion_condicion):
        condicion = input("1-ASCENDENTE.\n2-DECENDENTE\n")
        if (condicion is None):
            condicion = input("1-ASCENDENTE.\n2-DECENDENTE\n")
        else:
            if (condicion == "1"):
                verificacion_condicion = False
            elif (condicion == "2"):
                verificacion_condicion = False
            

    funcion_orden_ascendente_decendente_promedios(legajos, generos_estudiantes, notas_materias, nombres_estudiantes, promedios_alumnos, condicion)

    for i in range(posicion):
        print("---------------------------------")
        print(f"Datos del alumno:")
        print(f"Legajo: {legajos[i]}")
        print(f"Nombre: {nombres_estudiantes[i]}")
        print(f"Género: {generos_estudiantes[i]}")
        print("Materia_1\tMateria_2\tMateria_3\tMateria_4\tMateria_5")
        print(f"{notas_materias[i][0]}\t\t"
              f"{notas_materias[i][1]}\t\t"
              f"{notas_materias[i][2]}\t\t"
              f"{notas_materias[i][3]}\t\t"
              f"{notas_materias[i][4]}\n")
        print(f"Promedio de notas: {promedios_alumnos[i]}\n")
        
    
    
    return "Todos los alumnos fueron mostrados correctamente."


def funcion_orden_ascendente_decendente_promedios(legajos:list, generos_estudiantes:list, notas_materias:list, nombres_estudiantes:list, promedios_alumnos:list, condicion:str) -> list:

    """
    El metodo ordena segun el parametro "condicion" las lista segun el promedio de una forma ascendente o decendente.
    
    Args:
    legajos = Es una lista con los 30 legajos de los alumnos.

    generos_estudiantes = Es una lista con los 3 generos.

    notas_materias = Es una matriz para visualizar las notas en las 5 materias de los 30 alumnos.

    nombres_estudiantes = Es una lista con los 30 nombres de los alumnos.

    promedios_alumnos = Es una lista con los promedios de los 30 alumnos.

    condicion = Determina si ordena las listas y matriz de forma ascendente o decendente.

    Returns:
    
    """
    
    
    if (condicion == "1"):
        for i in range(0, len(promedios_alumnos)-1, 1):
        
            for j in range(i + 1, len(promedios_alumnos), 1):
                
                if promedios_alumnos[i] > promedios_alumnos[j] or (promedios_alumnos[i] == promedios_alumnos[j] and nombres_estudiantes[i] > nombres_estudiantes[j]):
                
                    promedio_auxiliar = promedios_alumnos[i]
                    promedios_alumnos[i] = promedios_alumnos[j]
                    promedios_alumnos[j] = promedio_auxiliar

                    nombre_auxiliar = nombres_estudiantes[i]
                    nombres_estudiantes[i] = nombres_estudiantes[j]
                    nombres_estudiantes[j] = nombre_auxiliar

                    genero_auxiliar = generos_estudiantes[i]
                    generos_estudiantes[i] = generos_estudiantes[j]
                    generos_estudiantes[j] = genero_auxiliar

                    legajo_auxiliar = legajos[i]
                    legajos[i] = legajos[j]
                    legajos[j] = legajo_auxiliar

                    nota_auxiliar = notas_materias[i]
                    notas_materias[i] = notas_materias[j]
                    notas_materias[j] = nota_auxiliar
    elif (condicion == "2"):
        for i in range(0, len(promedios_alumnos)-1, 1):
        
            for j in range(i + 1, len(promedios_alumnos), 1):
                
                if promedios_alumnos[i] < promedios_alumnos[j] or (promedios_alumnos[i] == promedios_alumnos[j] and nombres_estudiantes[i] > nombres_estudiantes[j]):
                
                    promedio_auxiliar = promedios_alumnos[i]
                    promedios_alumnos[i] = promedios_alumnos[j]
                    promedios_alumnos[j] = promedio_auxiliar

                    nombre_auxiliar = nombres_estudiantes[i]
                    nombres_estudiantes[i] = nombres_estudiantes[j]
                    nombres_estudiantes[j] = nombre_auxiliar

                    genero_auxiliar = generos_estudiantes[i]
                    generos_estudiantes[i] = generos_estudiantes[j]
                    generos_estudiantes[j] = genero_auxiliar

                    legajo_auxiliar = legajos[i]
                    legajos[i] = legajos[j]
                    legajos[j] = legajo_auxiliar

                    nota_auxiliar = notas_materias[i]
                    notas_materias[i] = notas_materias[j]
                    notas_materias[j] = nota_auxiliar


def mayor_promedio_materia(notas_materias:list) -> str:
    
    """
    Solicita y verifica si mostrar el promedio general de materias o materia con mayor promedio y lo envia junto a la lista notas_materias a una funcion.
    
    Args:

    notas_materias = Es una matriz de las notas en las 5 materias(columnas) de los 30 alumnos(filas).

    Returns:
    
    """
    validacion = True
    condicion = input("Ingrese condicion:\n1-Promedio general de materias.\n2-La materia con mayor promedio.\n")

    while (validacion):

        if (condicion is None):
            condicion = input("Ingrese condicion:\n1-Promedio general de materias.\n2-La materia con mayor promedio.\n")

        else:
            if (condicion == "1"):
                validacion = False
            elif (condicion == "2"):
                validacion = False
           
            else:
                condicion = input("Ingrese condicion:\n1-Promedio general de materias.\n2-La materia con mayor promedio.\n")
    

    mostrar_mayor_promedio_materia(notas_materias, condicion)

    return "Los datos fueron mostrados correctamente."

    
def mostrar_mayor_promedio_materia(notas_materias:list, condicion:str) -> str:

    """
    El metodo determina los promedios de notas de las materias y imprime en consola el promedio general de materias o la materia con mayor promedio.
    
    Args:

    notas_materias = Es una matriz de las notas en las 5 materias(columnas) de los 30 alumnos(filas).

    condicion = Determina si muestras todos los promedios de todas las materias o muestra con el mayor.

    Returns:
    

    """
    
    
    materia_1 = 0
    materia_2 = 0
    materia_3 = 0
    materia_4 = 0
    materia_5 = 0
    
    for o in range(30):  
        materia_1 += notas_materias[o][0]
        materia_2 += notas_materias[o][1]
        materia_3 += notas_materias[o][2]
        materia_4 += notas_materias[o][3]
        materia_5 += notas_materias[o][4]

    materia_1 = materia_1 / 30
    materia_2 = materia_2 / 30
    materia_3 = materia_3 / 30
    materia_4 = materia_4 / 30
    materia_5 = materia_5 / 30

    if (condicion == "1"):
        mensaje = (f"\nPromedio general de materias:\nMateria_1\t\t\tMateria_2\t\t\tMateria_3\t\t\tMateria_4\t\t\tMateria_5\n{materia_1}\t\t{materia_2}\t\t{materia_3}\t\t{materia_4}\t\t{materia_5}\2")
        print(mensaje)
      
        
    elif(condicion == "2"):
        mayor = materia_1
        materia_mayor = "Materia_1"

        if materia_2 > mayor:
            mayor = materia_2
            materia_mayor = "Materia_2"

        if materia_3 > mayor:
            mayor = materia_3
            materia_mayor = "Materia_3"

        if materia_4 > mayor:
            mayor = materia_4
            materia_mayor = "Materia_4"

        if materia_5 > mayor:
            mayor = materia_5
            materia_mayor = "Materia_5"

        mensaje = (f"\nLa materia con mayor promedio es {materia_mayor} con {mayor}\n")
        print(mensaje)

    
def buscar_calificacion_repetida(notas_materias:list, condicion:str)-> str:
    
    """
    Cuenta cuantas veces se repite cada calificación en una asignatura determinada.
    
    Args:

    notas_materias = Es una matriz de las notas en las 5 materias(columnas) de los 30 alumnos(filas).

    condicion = Contendra la meteria a promediar.

    Returns:
    Devuelve el promedio general de todas las materias o devuelve la materia con mayor promedio.

    """
    
    nota_1 = 0
    nota_2 = 0
    nota_3 = 0
    nota_4 = 0
    nota_5 = 0
    nota_6 = 0
    nota_7 = 0
    nota_8 = 0
    nota_9 = 0
    nota_10 = 0

    for i in range(30):
        match (notas_materias[i][int(condicion)]):
            case 1:
                nota_1 = nota_1 + 1
            case 2:
                nota_2 = nota_2 + 1
            case 3:
                nota_3 = nota_3 + 1
            case 4:
                nota_4 = nota_4 + 1
            case 5:
                nota_5 = nota_5 + 1
            case 6:
                nota_6 = nota_6 + 1
            case 7:
                nota_7 = nota_7 + 1
            case 8:
                nota_8 = nota_8 + 1
            case 9:
                nota_9 = nota_9 + 1
            case 10:
                nota_10 = nota_10 + 1

    mensaje = (f"Notas de Materia_{str(int(condicion)+1)}:\nCantidad de 1: {nota_1}\nCantidad de 2: {nota_2}\nCantidad de 3: {nota_3}\nCantidad de 4: {nota_4}\nCantidad de 5: {nota_5}\nCantidad de 6: {nota_6}\nCantidad de 7: {nota_7}\nCantidad de 8: {nota_8}\nCantidad de 9: {nota_9}\nCantidad de 10: {nota_10}\n")

    return mensaje


def numero_materia()-> str:
    
    """
    Solicita y verifica el numero de materia  
    
    Args:

    ninguno.
    
    Returns:
    Devuelve la meteria selecciona por el usuario.

    """
    
    validacion = True
    opcion = input("Ingrese numero de materia:\n1-Materia_1.\n2-Materia_2.\n3-Materia_3.\n4-Materia_4.\n5-Materia_5.\n")
    while (validacion):

        if (opcion is None):
            
            opcion = input("Ingrese numero de materia:\n1-Materia_1.\n2-Materia_2.\n3-Materia_3.\n4-Materia_4.\n5-Materia_5.\n")

        else:
            if (opcion == "1"):
                validacion = False
            elif (opcion == "2"):
                validacion = False
            elif (opcion == "3"):
                validacion = False
            elif (opcion == "4"):
                validacion = False
            elif (opcion == "5"):
                validacion = False
            else:
                opcion = input("Ingrese numero de materia:\n1-Materia_1.\n2-Materia_2.\n3-Materia_3.\n4-Materia_4.\n5-Materia_5.\n")

    opcion = str(int(opcion)-1)

    return opcion 


    

    
    
    


  
   
