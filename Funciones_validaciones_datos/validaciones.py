
def mensaje_home() -> str:
    return ("\n<<<<<<<<<<->>>>>>>>>>\nBienvenido EduSystem - Home\n\n1-Cargar datos de alumnos.\n2-Mostrar datos de alumnos.\n3-Calcular promedio de notas.\n4-Salir del programa\n<<<<<<<<<<->>>>>>>>>>\n")

def mensaje_carga_alumnos() -> str:
    return ("\n<<<<<<<<<<->>>>>>>>>>\nEduSystem - Alta de alumnos\n\n1-Cargar alumnos.\n2-Cargar notas.\n3-Salir.\n<<<<<<<<<<->>>>>>>>>>\n")

def mensaje_mostrar_alumnos() -> str:
    return ("\n<<<<<<<<<<->>>>>>>>>>\nEduSystem - Mostrar alumnos\n\n1-Mostrar un alumno.\n2-Mostrar todo.\n3-Salir.\n<<<<<<<<<<->>>>>>>>>>\n")

def mensaje_promedios_alumnos() -> str:
    return ("\n<<<<<<<<<<->>>>>>>>>>\nEduSystem - Promedios de alumnos\n\n1-Elegir alumno.\n2-Mostrar todos.\n3-Mayores promedios por materia\n4-Mayor promedio en materia\n5-Salir.\n<<<<<<<<<<->>>>>>>>>>\n")

def mensaje_ingresar_nombre_alumno(i:int) -> str:
    return (f"Ingrese el nombre del alumno n°{i+1}: ")

def mensaje_ingresar_genero_alumno(i:int) -> str:
    return (f"Ingrese el genero del alumno n°{i+1}(M-F-X): ")

def mensaje_ingresar_legajo_alumno(i:int) -> str:
    return (f"Ingrese el numero de legajo del alumno n°{i+1} (5 numeros): ")

def mensaje_ingresar_nota_alumno(i:int, x:int) -> str:
    return (f"Ingrese el nota de la materia n°{x+1} del alumno n°{i}: ")

def mensaje_mostrar_alumno() -> str:
    return("Ingrese un numero de legajo existente:")



def validar_home() -> str:
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
            else:
                opcion = input(mensaje_home())
        
    return opcion


def validar_opcion_1() -> str:
    validacion = True
    opcion = input(mensaje_carga_alumnos())

    while (validacion):

        if (opcion is None):
            opcion = input(mensaje_carga_alumnos())

        else:
            if (opcion == "1"):
                validacion = False
            elif (opcion == "2"):
                validacion = False
            elif (opcion == "3"):
                validacion = False
            else:
                opcion = input(mensaje_carga_alumnos())
        
    return opcion


def validar_opcion_2() -> str:
    validacion = True
    opcion = input(mensaje_mostrar_alumnos())

    while (validacion):

        if (opcion is None):
            opcion = input(mensaje_mostrar_alumnos())

        else:
            if (opcion == "1"):
                validacion = False
            elif (opcion == "2"):
                validacion = False
            elif (opcion == "3"):
                validacion = False
            else:
                opcion = input(mensaje_mostrar_alumnos())
        
    return opcion


def validar_opcion_3() -> str:
    validacion = True
    opcion = input(mensaje_promedios_alumnos())

    while (validacion):

        if (opcion is None):
            opcion = input(mensaje_promedios_alumnos())

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
                opcion = input(mensaje_promedios_alumnos())
        
    return opcion

def cargar_alumnos(nombres_estudiantes:list,  generos_estudiantes:list, legajos:list) -> str:
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

        validacion_genero = True
        while (validacion_genero):
            genero = input(mensaje_ingresar_genero_alumno(i))
            if (genero == "M"):
                validacion_genero = False
            elif (genero == "F"):
                validacion_genero = False   
            elif (genero == "X"):
                validacion_genero = False         
            else:
                validacion_genero = True 
        
        validacion_legajo = True
        while (validacion_legajo):
            numero_legajo = input(mensaje_ingresar_legajo_alumno(i))
            for o in (numero_legajo):
                cantidad = len(numero_legajo)
                if (cantidad == 5):
                    if (48 <= ord(o) <=57):
                        validacion_legajo = False    
                    else:
                        validacion_legajo = True
                        break         
                
       
        nombres_estudiantes[i] = nombre 
        generos_estudiantes[i] = genero
        legajos[i] = numero_legajo

    return ("Los 30 alumnos fueron cargados correctamente!")      
            

def cargar_notas_alumnos(nombres_estudiantes:list, notas_materias:list, promedios_alumnos:list) -> str:
    cantidad_alumnos = len(nombres_estudiantes)
    validacion = True
    
    for i in range(cantidad_alumnos):
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

        promedio = (notas_materias[i][0] + notas_materias[i][1] + notas_materias[i][2] + notas_materias[i][3] + notas_materias[i][4]) / 5
        promedios_alumnos[i] = promedio               

    return ("Las notas de los 30 alumnos fueron cargados correctamente!")    
        
def mostrar_un_alumno(legajos:list, generos_estudiantes:list, notas_materias:list, nombres_estudiantes:list) -> str:
    validacion = True
    posicion = None
    posicion_nombre_estudiantes = len(nombres_estudiantes)
    seleccion_alumno = True

    while (seleccion_alumno):
        for u in range(posicion_nombre_estudiantes):
            print(f"{u+1}-{nombres_estudiantes[u]}")

        numero_alumno = input("Seleccione un alumno:")
        if (numero_alumno is None):
            numero_alumno = input("Seleccione un alumno:")
        else:
            if (len(numero_alumno) == 2):
                    for x in (numero_alumno):
                        if (48 <= ord(x) <= 57):
                            validacion = False
                        else:
                            validacion = True
                            break
        
        if (validacion == False):
            for z in range(posicion_nombre_estudiantes):
                if (int(numero_alumno) == (z+1)):
                    posicion = z
                    seleccion_alumno = False
                    break

                
    return (
    f"Datos del alumno:\n"
    f"Legajo: {legajos[posicion]}\n"
    f"Nombre: {nombres_estudiantes[posicion]}\n"
    f"Género: {generos_estudiantes[posicion]}\n"
    "Materia_1\tMateria_2\tMateria_3\tMateria_4\tMateria_5\n"
    f"{notas_materias[posicion][0]}\t\t"
    f"{notas_materias[posicion][1]}\t\t"
    f"{notas_materias[posicion][2]}\t\t"
    f"{notas_materias[posicion][3]}\t\t"
    f"{notas_materias[posicion][4]}")




def mostrar_todos_alumnos(legajos:list, generos_estudiantes:list, notas_materias:list, nombres_estudiantes:list) -> str:
    posicion = len(legajos)

    for i in range(posicion):
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
    
    return "Todos los alumnos fueron mostrados correctamente."
   

def mostrar_alumno_legajo_promedio(legajos:list, generos_estudiantes:list, notas_materias:list, nombres_estudiantes:list, promedios_alumnos:list) -> str:
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


    return (
    f"Datos del alumno:\n"
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

def mostrar_todos_alumnos_promedio(legajos:list, generos_estudiantes:list, notas_materias:list, nombres_estudiantes:list, promedios_alumnos:list) -> str:
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
        
def mayor_promedio_materia(notas_materias:list, condicion:str) -> str:
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
        return(f"Promedio general de materias:\nMateria_1\t\t\tMateria_2\t\t\tMateria_3\t\t\tMateria_4\t\t\tMateria_5\n{materia_1}\t\t{materia_2}\t\t{materia_3}\t\t{materia_4}\t\t{materia_5}")
      
        
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

        return(f"La materia con mayor promedio es {materia_mayor} con {mayor}")

    

    
    
    


  
   
