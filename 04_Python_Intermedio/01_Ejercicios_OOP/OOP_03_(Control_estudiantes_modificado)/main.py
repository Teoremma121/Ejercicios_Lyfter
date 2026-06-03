import menu
import actions
import data

def main():
    data_base = []
    index = 0
    while True:
        index = menu.call_main_menu()
        if index in ["7","8"]:
            data_base = data.index_to_data_manage(index,data_base)
        else:
            actions.index_to_action(index,data_base)
            

main()