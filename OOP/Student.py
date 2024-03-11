class Student:
    # Hàm thiết lập (Constructor)
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
    def print_info(self):
        print("ID: " +self.id)
        print("Name: " +self.name)
        print("Grade: " + str(self.grade))


sv1 = Student("63130480", "Khánh Hưng", 8.5)
sv1.print_info()