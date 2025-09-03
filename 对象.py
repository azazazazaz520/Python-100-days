class Student:
    name = None
    gender = None
    nationality = None
    age = None
    native_place = None
    def __init__(self, name, gender, nationality, age, native_place):
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.age = age
        self.native_place = native_place

    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}, Nationality: {self.nationality}, Age: {self.age}, Native Place: {self.native_place}"
    def __lt__(self, other):
        return self.age < other.age
stu = Student("Alice", "Female", "American", 20, "New York")
stu1 = Student("Bob", "Male", "Canadian", 22, "Toronto")
print(stu.__str__())
print(stu < stu1)