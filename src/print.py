class Print():
    def __init__(self) -> None:
        pass

    def show_teacher_info(self, teacher):
        return f"Name:{teacher.name}    Family:{teacher.family} Id: {teacher.id}"
    

    def show_maneger_info(self, maneger):
        return f"Name: {maneger.name} Family: {maneger.family} Id: {maneger.id}"
    
    
    def show_student_info(self, student):
        return f"Name: {student.name} Family: {student.family} Id: {student.id}"
