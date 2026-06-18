import classes as cl
import interface as ifc
import storage as st
from pathlib import Path
import os
import csv


def test_init_Finance_Manager():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    result = fm.movements
    assert result == []

def test_method_create_category_checking_from_object_attributes():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.create_category('Trabajo','#8080c0')
    result = (fm.categories[0].name, fm.categories[0].color)
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    assert result == ('Trabajo','#8080c0')

def test_method_create_movement_checking_from_object_attributes():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.add_movement('25/04/2025','Gasto','Educación','Copias',5000)
    move = fm.movements[0]
    result = [move.date, move.type, move.category, move.title, move.amount]
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    assert result == ['25/04/2025','Gasto','Educación','Copias',-5000]

def test_add_movement_checking_from_csv():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.add_movement('25/03/2025','Ingreso','Trabajo','Quincena',350000)
    fm.add_movement('27/03/2025','Gasto','Comida','Diario',-150000)
    result = file_1.read_text(encoding="utf-8")
    expected = (
        "date,type,category,title,amount\n"
        "25/03/2025,Ingreso,Trabajo,Quincena,350000.0\n"
        "27/03/2025,Gasto,Comida,Diario,-150000.0\n"
    )
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    assert result == expected

def test_filter_by_date():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.add_movement('25/03/2025','Ingreso','Trabajo','Quincena',350000)
    fm.add_movement('27/03/2025','Gasto','Comida','Diario',-150000)
    rows = ifc.update_movements(fm)
    filtered_rows = ifc.filter_by_date(rows,'24/03/2025','26/03/2025')
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    result = filtered_rows[0]
    expected = ['25/03/2025','Ingreso','Trabajo','Quincena',350000]
    assert result == expected

def test_getting_info_from_existing_file():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    with open("categories.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name","color"])
        writer.writerow(["Educación", "#00ffff"])
        writer.writerow(["Salud", "#8080c0"])
    fm = cl.Finance_Manager()
    resultado = (fm.categories[0].name, fm.categories[1].name)
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    assert resultado == ('Educación','Salud')

