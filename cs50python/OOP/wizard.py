class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student:
    def __init__(self, name, house):
        super()._init__(name)
        self.house = house

        ...


class Professor:
    def __init__(self, name, subject):
        super()._init__(name)
        self.subject = subject

        ...


wizard = Wizard("Albus")
student = Student("Harry")
professor = Professor("Severus")
...