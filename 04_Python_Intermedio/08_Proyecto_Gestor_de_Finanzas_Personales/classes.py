import storage as st

class Finance_Manager():
    movements: list
    categories: list

    def __init__(self):
        self.movements = []
        self.categories = []
        st.check_if_files_exist(self)

    def add_movement(self,type,category,title,amount):
        self.movements.append(Movement(type,category,title,amount))
        st.write_movements(self)

    def create_category(self,name,color):
        self.categories.append(Category(name,color))
        st.write_categories(self)

class Movement():
    type: str
    category: str
    title: str
    amount: float

    def __init__(self,type,category,title,amount):
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




