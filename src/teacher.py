from src.member import Member

class Teacher(Member):
    def __init__(self, name, family, id):
        super().__init__(name, family, id)