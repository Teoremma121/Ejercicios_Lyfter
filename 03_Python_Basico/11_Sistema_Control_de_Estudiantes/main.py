import menu
import actions

def main():
    current_index = ["0"]
    while True:
        current_index = menu.navigate_menu(current_index)
        actions.index_to_action(".".join(current_index))
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
