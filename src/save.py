class Save():
    def __init__(self) -> None:
        pass

    def save_teacher_info(self, teacher):
        data = [teacher.name, teacher.family, teacher.id]
        return data

    def save_manager_info(self, manager):
        data = [manager.name, manager.family, manager.id]
        return data

    def save_student_info(self, student):
        data = [student.name, student.family, student.id]
        return data

