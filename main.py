from src.teacher import Teacher
from src.maneger import Maneger
from src.student import Student
from src.print import Print
from src.save import Save


def main():
    ali = Teacher('Ali', 'Alirezadeh', 123)
    reza = Maneger('Reza', 'Rezazadeh', 456)
    amir = Student('Amir', 'Amiri', 789)

    printer = Print()
    print(printer.show_teacher_info(ali))
    print(printer.show_maneger_info(reza))
    print(printer.show_student_info(amir))


    saver = Save()
    saver.save_teacher_info(ali)
    saver.save_manager_info(reza)
    saver.save_student_info(amir)


main()