import csv
headers = ['date','type','category','title','amount']

def check_if_files_exist(manager):
    try:
        read_categories(manager)
    except FileNotFoundError:
        write_categories(manager)
    try:
        read_movements(manager)
    except FileNotFoundError:
        write_movements(manager)

def write_movements(manager):
    movements_list = []
    for move_object in manager.movements:
        move_dict = {}
        for attribute in headers:
            move_dict[attribute] = str(getattr(move_object,attribute))
        movements_list.append(move_dict)

    with open("movements.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(movements_list)

def read_movements(manager):
    with open("movements.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['amount'] = abs(float(row['amount']))
            manager.add_movement(row['date'],row['type'],row['category'],row['title'],str(row['amount']))

def write_categories(manager):
    categories_list = []
    for cat_class in manager.categories:
        cat_dict = {}
        cat_dict['name'] = cat_class.name
        cat_dict['color'] = cat_class.color
        categories_list.append(cat_dict)

    with open("categories.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=['name','color'])
        writer.writeheader()
        writer.writerows(categories_list)

def read_categories(manager):
    with open("categories.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            manager.create_category(row['name'],row['color'])