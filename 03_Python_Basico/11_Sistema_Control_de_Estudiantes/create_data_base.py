names = []
asignatures = ['Spanish','English','Socials','Sciences','Math']
sections = {'7A':9,'7B':19,'7C':29,'8A':39,'8B':49,'8C':59,'9A':69,'9B':79,'9C':89}
grades = []

with open("pjs.txt",'r',encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        row = row.replace(","," ")
        names.append(row)

def random_grade():
    import random
    prob = random.random()    
    if prob < 0.2:           
        return random.uniform(0, 60)
    else:
        return random.uniform(60, 100)
    
for i in range(90):
    student = {}
    student['name'] = names[i]
    for section,number in sections.items():
        if i <= number:
            student['section'] = section
            break
    for asignature in asignatures:
        student[asignature] = round(random_grade(),2)
    grades.append(student)

headers = ['name','section','Spanish','English','Socials','Sciences','Math']
import csv
with open("notas.csv",'w',encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(grades)
print("La información ha sido exportada al archivo 'notas.csv'")


