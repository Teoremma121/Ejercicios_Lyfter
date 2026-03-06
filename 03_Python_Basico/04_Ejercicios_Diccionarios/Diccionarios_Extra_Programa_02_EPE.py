# Ejercicios Extra de Diccionarios - Python Básico
# Emmanuel Piedra Esquivel
# Programa 02:
# Agrupar empleados por departamento:
# Dada una lista de empleados donde cada uno tiene nombre, correo y departamento,
# cree un diccionario que agrupe los empleados por su departamento:

employees = [
    {"name": "Harry", "email": "harry.potter@hogwatz.com", "department": "Ventas"},
    {"name": "Hermione", "email": "hermione.granger@hogwatz.com", "department": "TI"},
    {"name": "Ron", "email": "ron.weasley@hogwatz.com", "department": "Ventas"},
    {"name": "Luna", "email": "luna.lovegood@hogwatz.com", "department": "RRHH"},
]

employees_per_department = {}

for employee in employees:
    if employees_per_department.get(employee["department"]) == None:
        employees_per_department[employee["department"]] = []
    employees_per_department[employee["department"]].append(employee["name"])

print(employees_per_department)

