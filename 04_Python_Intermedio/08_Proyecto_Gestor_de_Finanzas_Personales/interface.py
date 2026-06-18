import PySimpleGUI as sg
import classes as cl
import layouts as ly
import validations as vl
from datetime import datetime

def main():
    fm = cl.Finance_Manager()
    print(type(fm))
    interface_main_logic(fm)

def interface_main_logic(manager):
    window_1 = ly.permanent_manager_window(manager)
    while True:
        update_main_window(window_1,manager)
        event, values = window_1.read()
        if event != sg.WIN_CLOSED:
            if event in ('-INCOME-','-EXPENSE-'):
                income_or_expense_event(manager,event,values,window_1)
            if event == '-CATEGORY-':
                create_category_event(manager,event,values,window_1)
        else:
            window_1.close()
            break

def update_main_window(window,manager):
    table_rows = update_movements(manager)
    table_rows = filter_by_date(table_rows,window['-START-'].get(),window['-END-'].get())
    table_rows = filter_by_category(manager,window,table_rows)
    table_rows = filter_by_type(window,table_rows)
    window['-TABLE-'].update(values=table_rows)
    update_table_colors(window,manager)
    update_total_incomes_expenses_balance(window,table_rows)

def income_or_expense_event(manager,event,values,main_window):
    sub_window = ly.add_movement_window(manager,event)
    while True:
        event, values = sub_window.read()
        if (event == 'Agregar'):
            if vl.validate_add_movement(manager,values,sub_window):
                manager.add_movement(values['-DATE-'],values['-TYPE-'],values['-CATEGORY-'],values['-TITLE-'],values['-AMOUNT-'])
                main_window['-START-'].update(manager.minor_date)
                main_window['-END-'].update(manager.major_date)
                sub_window.close()
                return
        if event in ["Cancelar",sg.WIN_CLOSED]:
                sub_window.close()
                return

def create_category_event(manager,event,values,main_window):
    sub_window = ly.create_category_window()
    while True:
        event, values = sub_window.read()
        if event == '-COLOR-':
            if values['-COLOR-']:
                sub_window['-SAMPLE-'].update(background_color=values["-COLOR-"])
        if (event == 'Crear'):
            if vl.validate_add_category(manager,values,sub_window):
                manager.create_category(values['-NAME-'],values['-COLOR-'])
                add_category(main_window,manager)
                sub_window.close()
                return
        if event in ['Cancelar',sg.WIN_CLOSED]:
            sub_window.close()
            return

def add_category(main_window,manager):
    new_cat_name = manager.categories[-1].name
    new_cat_color = manager.categories[-1].color
    main_window.extend_layout(main_window["-CATS-"],[[sg.Checkbox(new_cat_name,default=True,key=f'-CAT-{new_cat_name.upper()}-',checkbox_color=new_cat_color,enable_events=True)]])

def update_movements(manager):
    rows = [[move.date, move.type, move.category, move.title, move.amount] for move in manager.movements]
    return rows

def update_table_colors(window,manager):
    table_widget = window["-TABLE-"].Widget
    category_names = []
    for cat in manager.categories:
        table_widget.tag_configure(cat.name, background=cat.color)
        category_names.append(cat.name)
    items = table_widget.get_children()

    for item in items:
        values = table_widget.item(item)["values"]
        category = values[2]

        for name in category_names:
            if category == name:
                table_widget.item(item, tags=(name,))

def filter_by_date(rows,start,end):
    start = datetime.strptime(start, "%d/%m/%Y")
    end = datetime.strptime(end, "%d/%m/%Y")
    filtered_list = []
    for row in rows:
        date = datetime.strptime(row[0], "%d/%m/%Y")
        if (date >= start) and (date <= end):
            filtered_list.append(row)
    return filtered_list

def filter_by_category(manager,window,rows):
    active_categories = [cat.name for cat in manager.categories]
    for key in window.key_dict.keys():
        if str(key).startswith('-CAT-'):
            if not window[key].get():
                for index,cat in enumerate(active_categories):
                    if f'-CAT-{cat.upper()}-' == key:
                        active_categories.pop(index)
                        break
    filtered_list = []
    for row in rows:
        if row[2] in active_categories:
            filtered_list.append(row)
    return filtered_list

def filter_by_type(window,rows):
    filtered_data = []
    active_tags = []
    if window['-CHECK-INCOMES-'].get():
        active_tags.append("Ingreso")
    if window['-CHECK-EXPENSES-'].get():
        active_tags.append("Gasto")
    for row in rows:
        if row[1] in active_tags:
            filtered_data.append(row)
    return filtered_data

def update_total_incomes_expenses_balance(window,rows):
    total_incomes = 0
    total_expenses = 0
    for row in rows:
        if row[1] == "Ingreso":
            total_incomes += row[4]
        else:
            total_expenses += row[4]

    window['-TOT-INCOMES-'].update(total_incomes)
    window['-TOT-EXPENSES-'].update(total_expenses)
    window['-BALANCE-'].update(total_expenses+total_incomes)


main()


