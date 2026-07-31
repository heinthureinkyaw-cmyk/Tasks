#task 4.2

import sqlite3
class Person:
    def __init__(self, full_name, date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def is_adult(self):
        birth_year = self.date_of_birth.split("-")[0]
        return (2020 - int(birth_year)) > 18

    def screen_name(self):
        raw_name = ""
        for char in self.full_name:
            if char.isalpha():
                raw_name += char

        year , month , day = self.date_of_birth.split("-")
        return raw_name + month + day


P = Person("John Tan" , "2000-06-01")

##print(P.is_adult())
##print(P.screen_name())


class Staff(Person):
    def is_adult(self):
        return True

    def screen_name(self):
        return super().screen_name() + "Staff"


S = Staff("John Tan" , "2000-06-01")
print(S.is_adult())
print(S.screen_name())



class Student(Person):
    def is_adult(self):
        return False




def process_file(filename, dbfile):
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()

    with open(filename, 'r') as file:
        for line in file:
            full_name, date_of_birth, role = line.strip().split(",")

            if role == "Staff":
                person = Staff(full_name, date_of_birth)
            elif role == "Student":
                person = Student(full_name, date_of_birth)
            else:
                person = Person(full_name, date_of_birth)

            screen_name = person.screen_name()
            is_adult = person.is_adult()

            cursor.execute("""
                INSERT INTO People (FullName, DateOfBirth, ScreenName, IsAdult)
                Values(?, ?, ?, ?)
            """, (full_name, date_of_birth, screen_name, is_adult))


    conn.commit()
    conn.close()

process_file('people.txt', 'school.db')
                
            
            
    






