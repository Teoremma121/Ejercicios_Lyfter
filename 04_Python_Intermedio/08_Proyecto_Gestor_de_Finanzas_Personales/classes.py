import storage as st
from datetime import datetime

class Finance_Manager():
    movements: list
    categories: list

    def __init__(self):
        self.movements = []
        self.categories = []
        st.check_if_files_exist(self)

    def add_movement(self,date,type,category,title,amount):
        amount = abs(float(amount))
        if type == 'Gasto':
            amount = -amount
        self.movements.append(Movement(date,type,category,title,amount))
        self.movements = sorted(self.movements,key=lambda move: datetime.strptime(move.date, "%d/%m/%Y"))
        st.write_movements(self)

    def create_category(self,name,color):
        self.categories.append(Category(name,color))
        st.write_categories(self)

class Movement():
    date: str
    type: str
    category: str
    title: str
    amount: float

    def __init__(self,date,type,category,title,amount):
        self.date = date
        self.type = type
        self.category = category
        self.title = title
        self.amount = amount

class Category():
    name: str
    color: str

    def __init__(self,name,color):
        self.name = name
        self.color = color




