import menu
import actions
import data

def main():
    data_base = []
    current_index = ["0"]
    while True:
        current_index = menu.navigate_menu(current_index)
        if ".".join(current_index) in ["0.5","0.6"]:
            data_base = data.index_to_data_manage(current_index,data_base)
        else:
            data_base = actions.index_to_action(current_index,data_base)
        current_index = after_action(current_index)

def after_action(main_index):
    sub_index = menu.call_back_or_exit_menu()
    if sub_index == "1":
        main_index.pop()
    elif sub_index == "2":
        main_index = ["0"]
    else:
        warning = menu.warning_lost_of_data()
        if warning == "1":
            exit()
        else:
            main_index = ["0"]
    return main_index

main()
