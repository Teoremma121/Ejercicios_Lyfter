names = []
asignatures = ['Spanish','English','Socials','Sciences','Math']
sections = {'7A':9,'7B':19,'7C':29,'8A':39,'8B':49,'8C':59,'9A':69,'9B':79,'9C':89}
grades = []

with open("pjs.txt",'r',encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        row = row.replace(","," ")
        names.append(row)

import random
for i in range(90):
    student = {}
    student['name'] = names[i]
    for section,number in sections.items():
        if i <= number:
            student['section'] = section
            break
    for asignature in asignatures:
        student[asignature] = round(random.uniform(0,100),2)
    grades.append(student)

# for index,student in enumerate(grades):
#     print(f"\n{index+1}) Nombre: {student['name']}")
#     print(f"Sección: {student['section']}")
#     print(f"Español: {student['Spanish']}")
#     print(f"Matemáticas: {student['Math']}")

headers = ['name','section','Spanish','English','Socials','Sciences','Math']
import csv
with open("notas.csv",'w',encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(grades)
print("La información ha sido exportada al archivo 'notas.csv'")


