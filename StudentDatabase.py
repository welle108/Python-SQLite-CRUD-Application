import Menu
import keyboard
import time


def main():
    menu = Menu.Menu()
    running = True
    Menu.Menu.main_menu()
    while running:
        selection = keyboard.read_key()
        time.sleep(1)
        if selection == '1':
            menu.display_students()
        elif selection == '2':
            menu.create_student()
        elif selection == '3':
            menu.update_record()
        elif selection == '4':
            menu.delete_student()
        elif selection == '5':
            menu.search_by()
        elif selection == "esc":
            exit(0)
        else:
            continue


if __name__ == '__main__':
    main()
