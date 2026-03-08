index_descriptions = {
                    "0.1.1":"Agregar un estudiante",
                    "0.1.2":"Editar un estudiante",
                    "0.1.3":"Eliminar un estudiante",
                    "0.2.1.1":"Mostrar estudiantes de una sección/alfabético",
                    "0.2.1.2":"Mostrar estudiantes de una sección/por promedio",
                    "0.2.1.3":"Mostrar estudiantes de una sección/resumen materia",
                    "0.2.2.1":"Mostrar estudiantes de una nivel/alfabético",
                    "0.2.2.2":"Mostrar estudiantes de una nivel/por promedio",
                    "0.2.2.3":"Mostrar estudiantes de una nivel/resumen materia",
                    "0.2.3":"Mostrar la información de un estudiante",
                    "0.3.1":"Top 3 de una sección",
                    "0.3.2":"Top 3 de todas las secciones",
                    "0.3.3":"Top 3 de un nivel",
                    "0.3.4":"Top 3 de todos los niveles",
                    "0.4.1":"Reprobados de una sección",
                    "0.4.2":"Reprobados de un nivel",
                    "0.4.3":"Reprobados de todos los niveles",
                    "0.5":"Exportar datos",
                    "0.6":"Importar datos",}

functions = [{"exit":["0.7","0.1.5","0.2.5","0.2.1.5","0.2.1.3.7","0.2.2.5","0.2.2.3.7","0.3.6","0.4.5"]}]

def index_to_action(index):
    if index in functions[0]['exit']:
        exit()
    else:
        print(index_descriptions[index])