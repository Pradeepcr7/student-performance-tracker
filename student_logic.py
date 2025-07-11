class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        total = sum(self.marks.values())
        subjects = len(self.marks)
        return total / subjects

    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        else:
            return "D"

    def get_results(self):
        for subject, mark in self.marks.items():
            if mark < 35:
                return "Fail"
        return "Pass"
