# Instrucciones
# Crea un API con Flask de que permita un CRUD (Create, Read, Update, Delete) de tareas.
# - Cada tarea debe tener:
#       - Identificador
#       - Título
#       - Descripción
#       - Estado (Por Hacer, En Progreso o Completada),
# - El API debe tener endpoints para:
#       - Obtener tareas.
#       - Esta debe tener un query parameter opcional para filtrarlas por Estado.
#       - Crear tareas.
#       - Editar tareas.
#       - Eliminar tareas.
# - Todos los datos deberán guardarse en un archivo JSON.
#       - Cada endpoint debe leer del archivo, y escribir en él (en caso de ser crear, editar o eliminar).
# - Además, debe de validar que:
#       - No se puedan agregar tareas con identificadores ya existentes.
#       - No se puedan agregar tareas sin nombre.
#       - No se pueden agregar tareas sin descripción.
#       - No se puedan agregar tareas sin estado.
#       - No se puedan agregar tareas con un estado invalido.

from flask import Flask, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)
app.json.sort_keys = False

base_dir = Path(__file__).resolve().parent
json_path = base_dir / "tasks.json"

def read_json():
    if json_path.exists():
        with open(json_path,'r',encoding='utf-8') as file:
            tasks_list = json.load(file)
    else:
        tasks_list = []
    return tasks_list

def write_json(updated_list):
    with open(json_path,'w',encoding='utf-8') as file:
        updated_list.sort(key=lambda x: x["id"])
        json.dump(updated_list,file,indent=3)

def check_if_id_exists(id, list):
    for task in list:
        if task['id'] == id:
            return True
    else:
        return False

def check_body_have_all_data(body):
        if "id" not in body:
            raise ValueError("No se digitó un id para la tarea")
        if "title" not in body:
            raise ValueError("No se digitó un título para la tarea")    
        if "description" not in body:
            raise ValueError("No se digitó una descripción para la tarea")    
        if "status" not in body:
            raise ValueError("No se digitó un estado para la tarea")
        if body.get("status") not in ["Por Hacer", "En Progreso", "Completada"]:
            raise ValueError("El estatus digitado no es válido")

@app.route("/tasks", methods = ['GET'])
def show_tasks():
    filtered_tasks = read_json()
    status_filter = request.args.get("status")
    if status_filter:
        filtered_tasks = list(filter(lambda task: task["status"] == status_filter, filtered_tasks))
    return filtered_tasks, 200

@app.route("/add", methods = ['POST'])
def add_task():
    try:
        check_body_have_all_data(request.json)
        id = request.json.get("id")
        if check_if_id_exists(id,read_json()):
            raise ValueError(f"Ya existe una tarea con el id: {id}")
        tasks_list = read_json()
        tasks_list.append(request.json)
        write_json(tasks_list)
        msg = f"Se agregó con éxito la tarea id: {id}"
        return jsonify(message=str(msg)), 200 
    except ValueError as e:
        return jsonify(Error=str(e)), 400    

@app.route("/edit/<id>", methods = ['PUT','PATCH'])
def edit_task(id):
    try:
        tasks_list = read_json()
        if not check_if_id_exists(id, tasks_list):
            raise ValueError(f"No existe una tarea con el id: {id}")
        for i, task in enumerate(tasks_list):
            if task["id"] == id:
                index = i
                break
        if request.method == 'PUT':
            check_body_have_all_data(request.json)
            new_id = request.json.get("id")
            if (id != new_id) and check_if_id_exists(new_id,tasks_list):
                raise ValueError(f"Ya existe una tarea con el nuevo id digitado: {new_id}")
            tasks_list[index] = request.json
            write_json(tasks_list)
            msg = f"Se reemplazó con éxito la tarea id: {id} --> id: {new_id}"
        else:
            new_id = id
            if "id" in request.json:
                new_id = request.json.get("id")
                if (id != new_id) and check_if_id_exists(new_id,tasks_list):
                    raise ValueError(f"Ya existe una tarea con el nuevo id digitado: {new_id}")
                tasks_list[index]["id"] = new_id
            if "title" in request.json:
                tasks_list[index]["title"] = request.json.get("title")
            if "description" in request.json:
                tasks_list[index]["description"] = request.json.get("description")
            if "status" in request.json:
                if request.json.get("status") not in ["Por Hacer", "En Progreso", "Completada"]:
                    raise ValueError("El estatus digitado no es válido")
                tasks_list[index]["status"] = request.json.get("status")
            write_json(tasks_list)
            msg = f"Se editó con éxito la tarea id: {id} --> id: {new_id}"
        return jsonify(message=str(msg)), 200
    except ValueError as e:
        return jsonify(Error=str(e)), 400    

@app.route("/remove/<id>", methods = ['DELETE'])
def remove_task(id):
    try:
        tasks_list = read_json()
        if not check_if_id_exists(id,tasks_list):
            raise ValueError(f"No existe una tarea con el id: {id}")
        for index, task in enumerate(tasks_list):
            if task["id"] == id:
                tasks_list.pop(index)
                break
        write_json(tasks_list)
        msg = f"Se eliminó con éxito la tarea id: {id}"
        return jsonify(message=str(msg)), 200
    except ValueError as e:
        return jsonify(Error=str(e)), 400  

if __name__ == "__main__":
    app.run(host="localhost", debug=True)