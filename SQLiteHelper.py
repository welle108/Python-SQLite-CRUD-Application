import time
import sqlite3
import Menu
import operator


class SQLiteHelper:
    temp_id = ''
    db_name = ''
    conn = ''
    c = ''

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    @staticmethod
    def display_row(row):
        for string in row:
            string = "{:<20}".format(string)
            print(string, end=" ")
        print('')

    def display_all_students(self, column, order):
        print()
        self.c.execute("SELECT * FROM  Students")
        rows = self.c.fetchall()
        rows.sort(key=operator.itemgetter(column), reverse=order)
        Menu.Menu.show_fields()
        for row in rows:
            self.display_row(row)
        print()
        print('                                Sort By:')
        print('-----------------------------------------------------------------------------------')
        print('1. GPA    2. Major    3. Adviser    q - Sort by Ascending  a - Sort by Descending')
        print('-----------------------------------------------------------------------------------')
        print()
        print('Press Backspace to return to main menu...')
        print()

    def display_student(self):
        student_id = input()
        running = True
        while running:
            self.c.execute('SELECT * FROM Students WHERE StudentId=?', (student_id,))
            student = self.c.fetchall()
            if len(student) == 0:
                print('Error: Please Enter Valid Student ID or type EXIT to quit')
                mod_id = input()
                if mod_id.lower() == "back":
                    running = False
                elif mod_id.lower() == "exit":
                    exit(0)
                continue
            else:
                self.temp_id = student[0][0]
                Menu.Menu.show_fields()
                for person in student:
                    self.display_row(person)
                print()
                running = False

    def display_by_parameter(self, param, condition, value):
        if param == 'GPA':
            if condition == '>':
                self.c.execute("SELECT GPA, FirstName, LastName FROM Students WHERE GPA>{}".format(value))
                rows = self.c.fetchall()
                rows.sort(key=operator.itemgetter(0))
                Menu.Menu.show_gpa_fields()
                for row in rows:
                    self.display_row(row)
                if len(rows) == 0:
                    print()
                    print('No entries match your search criteria')
                print()
                input('Hit Enter to return to main menu...')
                print()
            elif condition == '<':
                self.c.execute("SELECT GPA, FirstName, LastName FROM Students WHERE GPA<{}".format(value))
                rows = self.c.fetchall()
                rows.sort(key=operator.itemgetter(0), reverse=True)
                Menu.Menu.show_gpa_fields()
                for row in rows:
                    self.display_row(row)
                if len(rows) == 0:
                    print()
                    print('No entries match your search criteria')
                print()
                input('Hit Enter to return to main menu...')
                print()
            elif condition == '=':
                self.c.execute("SELECT GPA, FirstName, LastName FROM Students WHERE GPA={}".format(value))
                rows = self.c.fetchall()
                Menu.Menu.show_gpa_fields()
                for row in rows:
                    self.display_row(row)
                if len(rows) == 0:
                    print()
                    print('No entries match your search criteria')
                print()
                input('Hit Enter to return to main menu...')
                print()
        elif param == 'Major':
            self.c.execute("SELECT Major, FirstName, LastName FROM Students WHERE Major=?", (value,))
            rows = self.c.fetchall()
            rows.sort(key=operator.itemgetter(2))
            Menu.Menu.show_major_fields()
            for row in rows:
                self.display_row(row)
            if len(rows) == 0:
                print()
                print('No entries match your search criteria')
            print()
            input('Hit Enter to return to main menu...')
            print()
        elif param == 'FacultyAdviser':
            self.c.execute("SELECT FacultyAdviser, FirstName, LastName FROM Students WHERE FacultyAdviser=?", (value,))
            rows = self.c.fetchall()
            rows.sort(key=operator.itemgetter(2))
            Menu.Menu.show_faculty_fields()
            for row in rows:
                self.display_row(row)
            if len(rows) == 0:
                print()
                print('No entries match your search criteria')
            print()
            input('Hit Enter to return to main menu...')
            print()

    def create_student(self, first_name, last_name, gpa, major, faculty_adviser):
        data = (first_name, last_name, gpa, major, faculty_adviser)
        try:
            self.c.execute(
                    "INSERT INTO Students(FirstName, LastName, GPA, Major, FacultyAdviser)"
                    "VALUES(?,?,?,?,?)", data)
            self.conn.commit()
            student_id = self.c.lastrowid
            self.c.execute("SELECT * FROM Students WHERE StudentId=?", (student_id,))
            row = self.c.fetchone()
            print()
            print("Student Created: ")
            print()
            Menu.Menu.show_fields()
            self.display_row(row)
            return True

        except sqlite3.Error as e:
            print('An error has occurred: ', e.args[0])
            return False

    def update_student_record(self):
        print()
        running = True
        print('Enter StudentID of student you wish to modify')
        print('You may also enter BACK to return to main menu and EXIT to quit program...')
        mod_id = input()
        if mod_id.lower() == "back":
            running = False
        elif mod_id.lower() == "exit":
            exit(0)
        while running:
            self.c.execute('SELECT * FROM Students WHERE StudentId=?', (mod_id,))
            student = self.c.fetchall()
            if len(student) == 0:
                print('Error: Please Enter Valid Student ID or type EXIT to quit')
                mod_id = input()
                if mod_id.lower() == "back":
                    running = False
                elif mod_id.lower() == "exit":
                    exit(0)
                continue
            else:
                self.temp_id = student[0][0]
                print('Modify this student? Type Y or N')
                Menu.Menu.show_fields()
                for person in student:
                    self.display_row(person)
                print()
                confirm_modify = input()
                running = True
                while running:
                    if confirm_modify == 'y':
                        print()
                        print('Modify which field? Press 1 or 2 followed by')
                        print('ENTER or type BACK to return to main menu: ')
                        print('-----------------------------------------------')
                        print('1. Major    2. Faculty Adviser')
                        print()
                        incorrect_input = True
                        while incorrect_input:
                            time.sleep(1)
                            selection = input()
                            time.sleep(1)
                            if selection == '1':
                                print()
                                incorrect_input = True
                                major = input('Enter new Student Major: ')
                                while incorrect_input:
                                    if not major.isalpha():
                                        major = input('ERROR: Please enter new Major letters only: ')
                                    elif len(major) > 10:
                                        major = input('ERROR: Please enter new Major '
                                                      'using 10 character or less: ')
                                    else:
                                        incorrect_input = False
                                self.c.execute("UPDATE Students SET Major=? WHERE StudentId=?",
                                               (major, self.temp_id))
                                self.conn.commit()
                                self.c.execute("SELECT * FROM Students WHERE StudentId=?", (self.temp_id,))
                                new_record = self.c.fetchall()
                                Menu.Menu.show_fields()
                                for record in new_record:
                                    self.display_row(record)
                                incorrect_input = False
                            elif selection == '2':
                                print()
                                incorrect_input = True
                                major = input('Enter new Student Faculty Adviser: ')
                                while incorrect_input:
                                    if not major.isalpha():
                                        major = input('ERROR: Please enter new Major letters only: ')
                                    elif len(major) > 25:
                                        major = input('ERROR: Please enter new Major '
                                                      'using 25 character or less: ')
                                    else:
                                        incorrect_input = False
                                self.c.execute("UPDATE Students SET FacultyAdviser=? WHERE StudentId=?",
                                               (major, self.temp_id))
                                self.conn.commit()
                                self.c.execute("SELECT * FROM Students WHERE StudentId=?", (self.temp_id,))
                                new_record = self.c.fetchall()
                                Menu.Menu.show_fields()
                                for record in new_record:
                                    self.display_row(record)
                                incorrect_input = False
                            elif selection.lower() == 'back':
                                incorrect_input = False
                            else:
                                print('Error: Press 1 to modify Major, 2 to modify Faculty Adviser, '
                                      'and backspace to return to main menu')
                                continue
                        self.conn.commit()
                        is_running = False
                        print()
                        print('Entry modified and updated')
                        print()
                        input('Press Enter to return to main menu...')
                        break
                    elif confirm_modify == 'n':
                        print('Entry not modified')
                        print()
                        print()
                        is_running = False
                        break
                    else:
                        print('Error: Enter only Y or N to modify student record or EXIT to quit')
                        confirm_modify = input().lower()
            running = is_running

    def delete_student(self):
        running = True
        print()
        print('Enter StudentID of student you wish to delete')
        print('You may also enter BACK to return to main menu and EXIT to quit program...')
        delete_id = input()
        if delete_id.lower() == "back":
            running = False
        elif delete_id.lower() == "exit":
            exit(0)
        while running:
            self.c.execute('SELECT * FROM Students WHERE StudentId=?', (delete_id,))
            student = self.c.fetchall()
            if len(student) == 0:
                print('Error: Please Enter Valid Student ID or type EXIT to quit')
                delete_id = input()
                if delete_id.lower() == "back":
                    running = False
                elif delete_id.lower() == "exit":
                    exit(0)
                continue
            else:
                print('Delete this student? Type Y or N')
                Menu.Menu.show_fields()
                for person in student:
                    self.display_row(person)
                confirm_delete = input().lower()
                while True:
                    if confirm_delete == 'y':
                        self.c.execute('DELETE FROM Students WHERE StudentId=?', (delete_id,))
                        self.conn.commit()
                        running = False
                        print()
                        print('Entry deleted')
                        print()
                        break
                    elif confirm_delete == 'n':
                        print()
                        print('Entry not deleted')
                        print()
                        running = False
                        break
                    else:
                        print('Error: Enter only Y or N to delete or EXIT to quit')
                        confirm_delete = input().lower()


