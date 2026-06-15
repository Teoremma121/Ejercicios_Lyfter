import PySimpleGUI as sg
import classes as cl
import layouts as ly

def main():
    fm = cl.Finance_Manager()
    interface_main_logic(fm)

def interface_main_logic(manager):
    start = manager.movements[0].date
    end = manager.movements[-1].date
    window_1 = ly.permanent_manager_window(manager,start,end)
    while True:
        window_1['-TABLE-'].update(values=ly.update_and_filter_movements(manager,start,end))
        update_table_colors(window_1,manager)
        event, values = window_1.read()
    
        if event != sg.WIN_CLOSED:
            if event in ('-INCOME-','-EXPENSE-'):
                window_2 = ly.one_shot_movement_window(manager,event)
                event, values = window_2.read()
                if (event == 'Agregar') and (len(values) == 6):
                    manager.add_movement(values['-DATE-'],values['-TYPE-'],values['-CATEGORY-'],values['-TITLE-'],values['-AMOUNT-'])
                window_2.close()

            if event == '-CATEGORY-':
                window_2 = ly.one_shot_create_category_window()
                while True:
                    event, values = window_2.read()
                    if event == '-COLOR-':
                        window_2['-SAMPLE-'].update(background_color=values["-COLOR-"])
                    if (event == 'Crear') and (len(values) == 2):
                        manager.create_category(values['-NAME-'],values['-COLOR-'])
                        add_category(window_1,manager)
                        window_2.close()
                        break
                    if event in ['Cancelar',sg.WIN_CLOSED]:
                        window_2.close()
                        break
            
            if event in ('-START-','-END-'):
                start = values['-START-']
                end = values['-END-']

        else:
            window_1.close()
            break

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

def add_category(window,manager):
    new_cat_name = manager.categories[-1].name
    new_cat_color = manager.categories[-1].color
    window.extend_layout(window["-CATS-"],[[sg.Checkbox(new_cat_name,default=True,key=f'-{new_cat_name}-',checkbox_color=new_cat_color)]])


main()

