import PySimpleGUI as sg
import classes as cl
import layouts as ly

def main():
    fm = cl.Finance_Manager()
    interface_main_logic(fm)

def interface_main_logic(manager):
    window_1 = ly.permanent_manager_window(manager)
    while True:
        event, values = window_1.read()
        update_table_colors(window_1,manager)
        if event != sg.WIN_CLOSED:
            if event in ('-INCOME-','-EXPENSE-'):
                window_2 = ly.one_shot_movement_window(manager,event)
                event, values = window_2.read()
                if (event == 'Agregar') and (len(values) == 4):
                    manager.add_movement(values['-TYPE-'],values['-CATEGORY-'],values['-TITLE-'],values['-AMOUNT-'])
                window_2.close()
                window_1['-TABLE-'].update(values=ly.update_movements(manager))
                update_table_colors(window_1,manager)
            if event == '-CATEGORY-':
                window_2 = ly.one_shot_create_category_window()
                while True:
                    event, values = window_2.read()
                    if event == '-COLOR-':
                        window_2['-SAMPLE-'].update(background_color=values["-COLOR-"])
                    if (event == 'Crear') and (len(values) == 2):
                        manager.create_category(values['-NAME-'],values['-COLOR-'])
                        new_cat_name = manager.categories[-1].name
                        new_cat_color = manager.categories[-1].color
                        window_1.extend_layout(window_1["-CATS-"],[[sg.Checkbox(new_cat_name,default=True,key=f'-{new_cat_name}-',checkbox_color=new_cat_color)]])
                        window_2.close()
                        break
                    if event in ['cancelar',sg.WIN_CLOSED]:
                        window_2.close()
                        break
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

main()

