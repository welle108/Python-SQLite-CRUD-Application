# Class to store student information
# Setter methods return old value and update existing object attributes


class Student:
    student_id = 0
    first_name = ''
    last_name = ''
    gpa = 0
    major = ''
    faculty_adviser = ''

    def set_id(self, new_id):
        old_id = self.student_id
        self.student_id = new_id
        return old_id

    def set_first_name(self, new_name):
        old_first_name = self.first_name
        self.first_name = new_name
        return old_first_name

    def set_last_name(self, last_name):
        old_last_name = self.last_name
        self.last_name = last_name
        return old_last_name

    def set_gpa(self, new_gpa):
        old_gpa = self.gpa
        self.gpa = new_gpa
        return old_gpa

    def set_major(self, new_major):
        old_major = self.major
        self.major = new_major
        return old_major

    def set_faculty_adviser(self, new_faculty_adviser):
        old_faculty_adviser = self.faculty_adviser
        self.faculty_adviser = new_faculty_adviser
        return old_faculty_adviser

    def get_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_gpa(self):
        return self.gpa

    def get_major(self):
        return self.major

    def get_faculty_adviser(self):
        return self.faculty_adviser


