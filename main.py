from Funciones_validaciones_datos import validaciones

notas_materias = [
    [10, 10, 6, 10, 10], 
    [5, 6, 7, 8, 6], 
    [9, 9, 8, 10, 7], 
    [6, 5, 7, 6, 5], 
    [8, 8, 7, 9, 8],
    [5, 5, 6, 6, 7], 
    [10, 9, 10, 9, 10], 
    [4, 5, 6, 5, 4], 
    [6, 7, 6, 7, 6], 
    [9, 9, 8, 8, 9],
    [7, 6, 8, 7, 7], 
    [5, 6, 7, 5, 6], 
    [8, 9, 9, 8, 9], 
    [6, 6, 5, 7, 6], 
    [10, 10, 10, 10, 10],
    [4, 4, 5, 4, 5], 
    [7, 7, 8, 8, 7], 
    [5, 5, 5, 6, 5], 
    [9, 9, 9, 8, 9], 
    [6, 6, 6, 6, 6],
    [7, 8, 7, 8, 7], 
    [5, 4, 5, 4, 5], 
    [8, 8, 9, 9, 8], 
    [6, 7, 6, 7, 6], 
    [10, 9, 9, 10, 9],
    [4, 3, 4, 3, 4], 
    [6, 6, 7, 6, 6], 
    [9, 10, 9, 10, 9], 
    [5, 6, 5, 6, 5], 
    [7, 7, 7, 7, 7]
]
nombres_estudiantes = ["Matias", "Juan", "Maria", "Maximo" ,"Lucas" ,"Candela" ,"Maite" ,"Gonzalo", "Martina", "Camilo", "Tiara", "Camila", "Agustin", "Aron" ,"Emilia" ,"Ezequiel" ,"Sofia" ,"Thiago", "Sabrina", "Facundo", "Pamela", "Leonardo", "Leandro", "Vanesa" ,"Sandra" ,"Belen" ,"Joaquin" ,"Fernando", "Mia", "Wanda"]
generos_estudiantes = ["X", "M", "X", "F" ,"F" ,"F" ,"F" ,"F", "F", "F", "F", "F", "F", "F" ,"F" ,"F" ,"F" ,"F", "F", "F", "F", "F", "F", "F" ,"F" ,"F" ,"F" ,"F", "F", "F"]
legajos = [
    10001, 10002, 10003, 10004, 10005,
    10006, 10007, 10008, 10009, 10010,
    10011, 10012, 10013, 10014, 10015,
    10016, 10017, 10018, 10019, 10020,
    10021, 10022, 10023, 10024, 10025,
    10026, 10027, 10028, 10029, 10030
]

promedios_alumnos = [
    7, 8, 7, 10, 7,
    7, 2, 7, 1, 7,
    7, 7, 6, 7, 2,
    6, 7, 7, 5, 7,
    7, 3, 7, 7, 7,
    7, 7, 9, 7, 1
]

salir_programa = True

while (salir_programa):
    salir_programa_1 = True
    salir_programa_2 = True
    salir_programa_3 = True
    
    opcion = validaciones.validar_home()
    
    match(opcion):
        case "1":
            while (salir_programa_1):
                opcion_1 = validaciones.validar_opcion_1()
                match(opcion_1):
                    case "1":
                        print(validaciones.cargar_alumnos(nombres_estudiantes, generos_estudiantes, legajos))
                    case "2":
                        print(validaciones.cargar_notas_alumnos(nombres_estudiantes, notas_materias,promedios_alumnos))
                    case "3":
                        salir_programa_1 = False
        case "2":
           while (salir_programa_2):
                opcion_2 = validaciones.validar_opcion_2()
                match(opcion_2):
                    case "1":
                        print(validaciones.mostrar_un_alumno(legajos, generos_estudiantes, notas_materias, nombres_estudiantes))
                    case "2":
                        print(validaciones.mostrar_todos_alumnos(legajos, generos_estudiantes, notas_materias, nombres_estudiantes))
                    case "3":
                        salir_programa_2 = False    
        case "3":
            while (salir_programa_3):
                opcion_3 = validaciones.validar_opcion_3()
                match(opcion_3):
                    case "1":
                        print(validaciones.mostrar_alumno_legajo_promedio(legajos, generos_estudiantes, notas_materias, nombres_estudiantes, promedios_alumnos))
                    case "2":
                        print(validaciones.mostrar_todos_alumnos_promedio(legajos, generos_estudiantes, notas_materias, nombres_estudiantes, promedios_alumnos))
                    case "3":
                        condicion = "1"
                        print(validaciones.mayor_promedio_materia(notas_materias, condicion))
                    case "4":
                        condicion = "2"
                        print(validaciones.mayor_promedio_materia(notas_materias, condicion))
                    case "5":
                        salir_programa_3 = False 
        case "4":
            print("OPCION 4")