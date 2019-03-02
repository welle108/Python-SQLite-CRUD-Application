import SQLiteHelper
import time
import keyboard


class IncorrectGPAFormat(Exception):
    """Raised when GPA is >4 or less than 0"""
    pass


class Menu:
    helper = ''
    temp_first_name = ''
    temp_last_name = ''
    temp_gpa = ''
    temp_major = ''
    temp_faculty_adviser = ''
    temp_running = True

    def __init__(self):
        self.helper = SQLiteHelper.SQLiteHelper('StudentDatabase.db')

    @staticmethod
    def main_menu():
        print('------------------------------------------------------')
        print('                Student Database')
        print('------------------------------------------------------')
        print('Enter the number of the option you wish to select:')
        print()
        print('1. Display All Students')
        print('2. Create Student')
        print('3. Update Student')
        print('4. Delete Student')
        print('5. Search')
        print()
        print('Enter 1-5 to make a selection or hit escape to quit')

    @staticmethod
    def refresh_main_menu():
        print('------------------------------------------------------')
        print('                Student Database')
        print('------------------------------------------------------')
        print('Enter the number of the option you wish to select:')
        print()
        print('1. Display All Students')
        print('2. Create Student')
        print('3. Update Student')
        print('4. Delete Student')
        print('5. Search')
        print()
        print('Enter 1-5 to make a selection or hit escape to quit')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()

    @staticmethod
    def show_fields():
        fields = ('Student ID', 'First Name', 'Last Name', 'GPA', 'Major', 'Faculty Adviser')
        print('\n' + '-' * 130)
        for string in fields:
            string = "{:<20}".format(string)
            print(string, end=" ")
        print('\n' + '-' * 130)

    @staticmethod
    def show_gpa_fields():
        fields = ('GPA', 'First Name', 'Last Name')
        print('\n' + '-' * 60)
        for string in fields:
            string = "{:<20}".format(string)
            print(string, end=" ")
        print('\n' + '-' * 60)

    @staticmethod
    def show_major_fields():
        fields = ('Major', 'First Name', 'Last Name')
        print('\n' + '-' * 60)
        for string in fields:
            string = "{:<20}".format(string)
            print(string, end=" ")
        print('\n' + '-' * 60)

    @staticmethod
    def show_faculty_fields():
        fields = ('Faculty Adviser', 'First Name', 'Last Name')
        print('\n' + '-' * 60)
        for string in fields:
            string = "{:<20}".format(string)
            print(string, end=" ")
        print('\n' + '-' * 60)

    def display_students(self):
        self.helper.display_all_students(0, False)
        time.sleep(1)
        curr_order = False
        curr_sort = 0
        while True:
            selection = keyboard.read_key()
            time.sleep(1)
            if selection == '1':
                curr_sort = 3
            elif selection == '2':
                curr_sort = 4
            elif selection == '3':
                curr_sort = 5
            elif selection == 'q':
                curr_order = False
            elif selection == "a":
                curr_order = True
            elif selection == 'backspace':
                self.refresh_main_menu()
                time.sleep(1)
                break
            else:
                continue
            self.helper.display_all_students(curr_sort, curr_order)

    def create_student(self):
        print()
        incorrect_input = True
        self.temp_first_name = input('Enter first name: ')
        while incorrect_input:
            if not self.temp_first_name.isalpha():
                self.temp_first_name = input('ERROR: Please enter letters only: ')
            elif len(self.temp_first_name) > 25:
                self.temp_first_name = input('ERROR: Please enter 25 character or less: ')
            else:
                incorrect_input = False
        incorrect_input = True
        self.temp_last_name = input('Enter last name: ')
        while incorrect_input:
            if not self.temp_last_name.isalpha():
                self.temp_last_name = input('ERROR: Please enter letters only: ')
            elif len(self.temp_last_name) > 25:
                self.temp_last_name = input('ERROR: Please enter 25 character or less: ')
            else:
                incorrect_input = False
        incorrect_input = True
        self.temp_gpa = input('Enter Student GPA: ')
        while incorrect_input:
            try:
                self.temp_gpa = float(self.temp_gpa)
                if self.temp_gpa > 4.0:
                    print('GPA too high')
                    raise IncorrectGPAFormat
                elif self.temp_gpa < 0:
                    print('GPA too low')
                    raise IncorrectGPAFormat
                else:
                    incorrect_input = False
            except (ValueError, IncorrectGPAFormat):
                self.temp_gpa = input('Enter Student GPA: ')
                continue
        incorrect_input = True
        self.temp_major = input('Enter Student Major: ')
        while incorrect_input:
            if not self.temp_major.isalpha():
                self.temp_major = input('ERROR: Please enter letters only: ')
            elif len(self.temp_major) > 10:
                self.temp_major = input('ERROR: Please enter 10 character or less: ')
            else:
                incorrect_input = False
        incorrect_input = True
        self.temp_faculty_adviser = input('Enter Faculty Adviser: ')
        while incorrect_input:
            if not self.temp_faculty_adviser.isalpha():
                self.temp_faculty_adviser = input('ERROR: Please enter letters only: ')
            elif len(self.temp_faculty_adviser) > 25:
                self.temp_faculty_adviser = input('ERROR: Please enter 25 character or less: ')
            else:
                incorrect_input = False
        self.helper.create_student(self.temp_first_name, self.temp_last_name,
                                   self.temp_gpa, self.temp_major, self.temp_faculty_adviser)
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        input('Press Enter to continue...')
        self.refresh_main_menu()

    def update_record(self):
        self.helper.update_student_record()
        self.refresh_main_menu()

    def delete_student(self):
        self.helper.delete_student()
        self.refresh_main_menu()

    def search_by(self):
        print()
        print()
        print('         Which value would you like to search?')
        print('---------------------------------------------------------')
        print('1. StudentID    2. GPA    3. Major    4. Faculty Adviser')
        print()
        print('Press backspace to return to main menu...')
        running = True
        while running:
            selection = keyboard.read_key()
            time.sleep(1)
            if selection == '1':
                print()
                print()
                print('Enter StudentID of Student you wish to view: ')
                self.helper.display_student()
                print()
                print('Press ENTER to return to main menu...')
                input()
                self.temp_running = False
            elif selection == '2':
                print()
                print()
                print('Enter GPA value search parameter: ')
                temp_gpa = input()
                print()
                incorrect_input = True
                while incorrect_input:
                    try:
                        temp_gpa = float(temp_gpa)
                        if temp_gpa > 4.0:
                            print('GPA too high')
                            raise IncorrectGPAFormat
                        elif temp_gpa < 0:
                            print('GPA too low')
                            raise IncorrectGPAFormat
                        else:
                            incorrect_input = False
                    except (ValueError, IncorrectGPAFormat):
                        print('Enter GPA value search parameter: ')
                        temp_gpa = input()
                        continue
                print('Sort results by: ')
                print('-----------------------------------------------')
                print('1. Greater Than    2. Less Than    3. Equals')
                while True:
                    time.sleep(1)
                    selection = keyboard.read_key()
                    time.sleep(1)
                    if selection == '1':
                        print()
                        self.helper.display_by_parameter('GPA', '>', temp_gpa)
                        break
                    elif selection == '2':
                        print()
                        self.helper.display_by_parameter('GPA', '<', temp_gpa)
                        break
                    elif selection == '3':
                        print()
                        self.helper.display_by_parameter('GPA', '=', temp_gpa)
                        break
                    else:
                        print('Error: Please type only 1-3 for sorting options...')
                        print()
                self.temp_running = False
                break
            elif selection == '3':
                print()
                print()
                print('Enter Major search criteria: ')
                temp_major = input()
                incorrect_input = True
                while incorrect_input:
                    if not temp_major.isalpha():
                        temp_major = input('ERROR: Please enter letters only: ')
                    elif len(temp_major) > 10:
                        temp_major = input('ERROR: Please enter 10 character or less: ')
                    else:
                        incorrect_input = False
                self.helper.display_by_parameter('Major', '', temp_major)
                self.temp_running = False
                break
            elif selection == '4':
                print()
                print()
                print('Enter Faculty Adviser search criteria: ')
                temp_adviser = input()
                incorrect_input = True
                while incorrect_input:
                    if not temp_adviser.isalpha():
                        temp_adviser = input('ERROR: Please enter letters only: ')
                    elif len(temp_adviser) > 25:
                        temp_adviser = input('ERROR: Please enter 10 character or less: ')
                    else:
                        incorrect_input = False
                self.helper.display_by_parameter('FacultyAdviser', '', temp_adviser)
                self.temp_running = False
                break
            elif selection == "backspace":
                self.temp_running = False
                break
            running = self.temp_running
        self.refresh_main_menu()

    @staticmethod
    def cls():
        print('\n'*5)


